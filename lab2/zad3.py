import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm as cm
import random
import sys
import networkx as nx

#  E:\agh\4s\mownit\lab2\siatka.txt

def add_edge(G,u,v,w=random.randint(5,10)):
    if G.has_edge(u,v):
        e=G.edges[u,v]
        if e['weight'] is None: w['weight']=w
        else: e['weight']=e['weight'] * w / (e['weight'] + w)
    else:G.add_edge(u,v,loops=[],volt=None,weight=w)
    return G.edges[u,v]

def applyVolt(G,u,v,volt):
    if G.has_edge(u,v):G.edges[u,v]['volt']=volt
    else: G.add_edge(u,v,loops=[],volt=volt,curr=None,weight=0)


def getCubeGrapch():
    edges = [
        [0,1,1],
        [0,5,1],
        [0,4,3],
        [1,2,10],
        [1,6,1],
        [2,3,5],
        [2,7,10],
        [3,5,7],
        [3,8,1],
        [4,9,1],
        [5,7,1],
        [5,8,10],
        [6,9,5],
        [6,8,2],
        [7,9,15]
    ]
    nodes = set()
    for v1, v2, _ in edges:
        nodes.add(v1)
        nodes.add(v2)

    nu, nv, nw = edges[-1]
    edges = edges[:-1]
    data = nx.empty_graph(len(nodes))
    [add_edge(data, u, v, w) for u, v, w in edges]
    applyVolt(data, nu, nv, nw)
    return data

def genCykl(nodes):
    G=nx.complete_graph(nodes)
    G.add_edge(nodes-1,nodes)
    for(u,v)in G.edges():
        G.edges[u,v]['weight']=random.randint(5,20)
        G.edges[u,v].update(loops=[],volt=None,curr=None)
        print(u,v,G.edges[u,v]['weight'])
    applyVolt(G,0,nodes-2,10)
    print(0,nodes-1,10)
    return G

def getGrid(nodes):
    G=nx.grid_2d_graph(nodes,nodes)
    for (u,v) in G.edges():
        G.edges[u,v]['weight']=random.randint(5,20)
        G.edges[u,v].update(loops=[],volt=None,curr=None)
        print(u,v,G.edges[u,v]['weight'])
    applyVolt(G,(0, 2), (0, 1), 15)
    return G


def show(G):
    pos = nx.spring_layout(G, k=3 / (len(G.nodes()) ** (1 / 2)), scale=2.0)
    attrs = nx.get_edge_attributes(G, 'curr')
    edges, labels = zip(*attrs.items())
    nx.draw_networkx(G, pos, edgelist=edges,
                     edge_color=labels,
                     alpha=0.2,
                     node_size=10,
                     edge_cmap=cm.YlOrRd,
                     font_size=8,
                     draw_labels=False
                     )
    attrs = {k: "{:.2f}A".format(v) for k, v in attrs.items()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=attrs, font_size=5, alpha=0.5)
    plt.axis('off')
    plt.show()


def solution(cirle):
    meshes=nx.cycle_basis(cirle)
    res=np.zeros(len(meshes))

    # выбираем циклы
    for i,mesh in enumerate(meshes):
        mesh=[*mesh,mesh[0]]
        for u,v in zip(mesh[:-1],mesh[1:]):
            if cirle.edges[u,v]['volt'] is not None: res[i]=cirle.edges[u,v]['volt']
            cirle.edges[u,v]['loops'].append((i,(u,v)))
    lin=np.zeros((len(meshes),len(meshes)))


    # меш анализ
    for i, mesh in enumerate(meshes):
        mesh = [*mesh, mesh[0]]
        for u, v in zip(mesh[:-1], mesh[1:]):
            for loop, vec in cirle.edges[u, v]['loops']:
                lin[i][loop] += (1 if vec == (u, v) else -1) * cirle.edges[u, v]['weight']

    loop_currents = np.linalg.solve(lin, res)

    # расчет для резистанций
    to_remove = []
    for (n, m) in cirle.edges():
        current = sum([(1 if vec == (n, m) else -1) * loop_currents[i] for i, vec in cirle.edges[n, m]['loops']])
        to_remove.append((n, m) if current > 0 else (n, m))
        edge = cirle.edges[n, m]
        edge['curr'] = abs(current)
        edge['volt'] = edge['volt'] if edge['volt'] is not None else edge['weight'] * current

    # граф направленный
    cirle = cirle.to_directed(as_view=False)

    for n, m in to_remove:
        cirle.remove_edge(n, m)
    return loop_currents, cirle





if __name__ == "__main__":
    data = None
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            edges = [[int(u), int(v), int(w)] for u, v, w in [line.split(' ') for line in f.readlines()]]
            nodes = set()
            for v1, v2, _ in edges:
                nodes.add(v1)
                nodes.add(v2)

            nu, nv, nw = edges[-1]
            edges = edges[:-1]
            data = nx.empty_graph(len(nodes))
            [add_edge(data, u, v, w) for u, v, w in edges]
            applyVolt(data, nu, nv, nw)
    else:
        data = genCykl(100)
        #data=getCubeGrapch()
        #data=getGrid(4)



    _, graph = solution(data)
    show(graph)






