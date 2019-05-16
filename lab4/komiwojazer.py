import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm as cm
import random
import sys
import networkx as nx

mini=0
maxi=15

def getPointsInOrder(n):
    a=[]
    for i in range(n):
        a.append([i,i])
    return np.array(a)



def getPoints(n):
    a=[]
    for i in range(n):
        a.append([random.randint(mini,maxi),random.randint(mini,maxi)])
    return np.array(a)

def getGroupPoints(g,p):
    a=[]
    i=0
    while(i<p):
        c = [random.uniform(mini, maxi), random.uniform(mini, maxi)]
        for j in range(int(p/g)):
            if(i<p):
                rx=random.uniform(-maxi/(2*g),maxi/(2*g))
                ry = random.uniform(-maxi/(2*g), maxi/ (2*g))
                a.append([c[0]+rx,c[1]+ry])
                i+=1
        print(c)
        print()
    return np.array(a)


def getNextSeq(seq):
    i=random.randint(0,len(seq)-1)
    j=random.randint(0,len(seq)-1)
    nextSeq=seq.copy()
    if(i>j):
        flip(j,i,nextSeq)
    else:
        flip(i,j,nextSeq)
    return nextSeq

def flip(i,j,seq):
    while(i<j):
        tmp=[seq[i,0],seq[i,1]]
        seq[i]=seq[j]
        seq[j]=tmp
        i+=1
        j-=1


def getCost(points):
    c=0
    for i in range(1,len(points)):
       c+=(points[i-1,0]-points[i,0])**2+(points[i-1,1]-points[i,1])**2
    return c

def getTemp(t,i):
    #return t*0.1/i
    #return t*0.97
    return 
    #return np.exp(t)

def transition(dE,t):
    if(t>0):
        return (random.random()<(np.exp(-dE/t)))
    else: return False

def plot(points, color='b', plot_last=True):
    x=[]
    y=[]
    for i in range(len(points)):
        x.append(points[i,0])
        y.append(points[i,1])
    if(plot_last):
        plt.plot(x, y, 'ro')
    for i in range(0, len(points) - 1):
        plt.plot([points[i,0], points[(i+1),0]], [points[i,1], points[(i+1),1]], lw=1, c=color)
    if plot_last:
        i = len(points) - 1
        plt.plot([points[i,0], points[0,0]], [points[i,1], points[0,1]], lw=1, c=color)
    plt.show()


def annealing(seq,t,endT,itr):
    i = 1
    curCost=getCost(seq)
    costs = []

    while(i<itr or t>endT):
        nextSeq=getNextSeq(seq)
        nextCost=getCost(nextSeq)

        if(nextCost<curCost):
            costs.append([i, curCost])
            curCost=nextCost
            seq=nextSeq
        else:
            if(transition(nextCost-curCost,t)):
                costs.append([i, curCost])
                curCost=nextCost
                seq=nextSeq
        if(t>endT):
            t=getTemp(t,i)
            print("TEMP: ",t)
        i+=1
    print(t)
    print(i)
    plot(seq,'green')
    plot(np.array(costs),'blue',False)



def main():
    n=100
    t=n*300
    endT=0.01
    itr=3000

    #points = getGroupPoints(3, n)
    points=getPoints(n)
    #points=getPointsInOrder(n)
    plot(points,'red')

    annealing(points,t,endT,itr)



main()