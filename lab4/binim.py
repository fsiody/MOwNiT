import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm as cm
import random
import sys
import networkx as nx
import time
import imageio as imageio



size = 100
density = 0.6
report = 20

startAll=time.time()


def main():
    #density = 0.2
    t = 1000
    endT = 0.01
    itr = 1000

    #getFile()
    black=[]
    #f=open("./black512", "r")
   # e=f.readline()
    #lines=f.readlines()
    #for l in lines:
     #   x=l.replace("(","").replace(")","").replace("\n","").split(",")
      #  print(x)
       # black.append((int(x[0]),int(x[1])))

    black = getStartIm(size, density)
    showIm(size,black)

    annealing(black, t, endT, itr)



def getFile():
    black = getStartIm(size, density)
    #e=getEnergy(black)
    with open("./black512", "w+") as f:
     #   f.write(str(e))
        for b in black:
            f.write("\n")
            f.write(str(b))

def showIm(size, black):
    figure=plt.figure(figsize=[10,10])
    ax=figure.add_subplot(1,1,1)
    #ax.set_position([0,0,1,1])
    #ax.set_axis_off()
    ax.set_xlim(-1,size)
    ax.set_ylim(-1,size)
    #ax.dpi=np.ceil(size/8)
    x=[]
    y=[]
    for i in range(len(black)):
        x.append(black[i][1])
        y.append(black[i][0])
    ax.plot(x,y,'s',markersize=7,markerfacecolor='k', markeredgewidth=0)
    plt.show()
    print(len(x))

def getNeigs(black, point):
    return getNeigs8(black, point)


def getNeigs12_(black, point):
    #  +
    # +--
    #+-O-+
    # --+
    #  +
    nghb = 0
    candidate = getCoord(point, -1, 0)
    if (candidate in black): nghb-=1
    candidate = getCoord(point, +1, 0)
    if (candidate in black): nghb-=1
    candidate = getCoord(point, 0, -1)
    if (candidate in black): nghb-=1
    candidate = getCoord(point, 0, +1)
    if (candidate in black): nghb-=1
    candidate = getCoord(point, -1, -1)
    if (candidate in black): nghb-=1
    candidate = getCoord(point, +1, -1)
    if (candidate in black): nghb+=1
    candidate = getCoord(point, -1, +1)
    if (candidate in black): nghb+=1
    candidate = getCoord(point, +1, +1)
    if (candidate in black): nghb-=1


    candidate = getCoord(point, -2, 0)
    if (candidate in black): nghb+=1
    candidate = getCoord(point, +2, 0)
    if (candidate in black): nghb+=1
    candidate = getCoord(point, 0, +2)
    if (candidate in black): nghb+=1
    candidate = getCoord(point, 0, -2)
    if (candidate in black): nghb+=1
    return nghb

def getNeigs121(black, point):
    #  +
    # +-+
    #+-O-+
    # +-+
    #  +
    nghb = 0
    candidate = getCoord(point, -1, 0)
    if (candidate in black): nghb-=1
    candidate = getCoord(point, +1, 0)
    if (candidate in black): nghb-=1
    candidate = getCoord(point, 0, -1)
    if (candidate in black): nghb-=1
    candidate = getCoord(point, 0, +1)
    if (candidate in black): nghb-=1

    candidate = getCoord(point, -1, -1)
    if (candidate in black): nghb+=1
    candidate = getCoord(point, +1, -1)
    if (candidate in black): nghb+=1
    candidate = getCoord(point, -1, +1)
    if (candidate in black): nghb+=1
    candidate = getCoord(point, +1, +1)
    if (candidate in black): nghb+=1


    candidate = getCoord(point, -2, 0)
    if (candidate in black): nghb+=1
    candidate = getCoord(point, +2, 0)
    if (candidate in black): nghb+=1
    candidate = getCoord(point, 0, +2)
    if (candidate in black): nghb+=1
    candidate = getCoord(point, 0, -2)
    if (candidate in black): nghb+=1
    return nghb
def getNeigs12(black, point):
    #  -
    # -+-
    #-+O+-
    # -+-
    #  -
    nghb = 0
    candidate = getCoord(point, -1, 0)
    if (candidate in black): nghb+=1
    candidate = getCoord(point, +1, 0)
    if (candidate in black): nghb+=1
    candidate = getCoord(point, 0, -1)
    if (candidate in black): nghb+=1
    candidate = getCoord(point, 0, +1)
    if (candidate in black): nghb+=1

    candidate = getCoord(point, -1, -1)
    if (candidate in black): nghb-=1
    candidate = getCoord(point, +1, -1)
    if (candidate in black): nghb-=1
    candidate = getCoord(point, -1, +1)
    if (candidate in black): nghb-=1
    candidate = getCoord(point, +1, +1)
    if (candidate in black): nghb-=1


    candidate = getCoord(point, -2, 0)
    if (candidate in black): nghb-=1
    candidate = getCoord(point, +2, 0)
    if (candidate in black): nghb-=1
    candidate = getCoord(point, 0, +2)
    if (candidate in black): nghb-=1
    candidate = getCoord(point, 0, -2)
    if (candidate in black): nghb-=1
    return nghb

def getNeigs20X(black, point):
    #   +
    #  ---
    # +-o-+
    #  ---
    #   +
    nghb = 0
    candidate = getCoord(point, -1, 0)
    if (candidate in black): nghb-=1
    candidate = getCoord(point, +1, 0)
    if (candidate in black): nghb-=1
    candidate = getCoord(point, 0, -1)
    if (candidate in black): nghb-=1
    candidate = getCoord(point, 0, +1)
    if (candidate in black): nghb-=1
    candidate = getCoord(point, -1, -1)
    if (candidate in black): nghb-=1
    candidate = getCoord(point, +1, -1)
    if (candidate in black): nghb+=1
    candidate = getCoord(point, -1, +1)
    if (candidate in black): nghb+=1
    candidate = getCoord(point, +1, +1)
    if (candidate in black): nghb-=1


    candidate = getCoord(point, -2, 0)
    if (candidate in black): nghb+=1
    candidate = getCoord(point, +2, 0)
    if (candidate in black): nghb+=1
    candidate = getCoord(point, 0, +2)
    if (candidate in black): nghb+=1
    candidate = getCoord(point, 0, -2)
    if (candidate in black): nghb+=1
    return nghb



def getNeigs8(black, point):
    # +++
    # +o+
    # +++
    nghb = 0
    candidate=getCoord(point,-1,0)
    if (candidate in black): nghb+=1
    candidate = getCoord(point, +1, 0)
    if (candidate in black): nghb+=1
    candidate = getCoord(point, 0, -1)
    if (candidate in black): nghb+=1
    candidate = getCoord(point, 0, +1)
    if (candidate in black): nghb+=1
    candidate = getCoord(point, -1, -1)
    if (candidate in black): nghb+=1
    candidate = getCoord(point, +1, -1)
    if (candidate in black): nghb+=1
    candidate = getCoord(point, -1, +1)
    if (candidate in black): nghb+=1
    candidate = getCoord(point, +1, +1)
    if (candidate in black): nghb+=1
    return nghb


def getNeigs4X(black, point):
    nghb = 0
    candidate=getCoord(point,-1,-1)
    if (candidate in black): nghb+=1
    candidate = getCoord(point, +1, -1)
    if (candidate in black): nghb+=1
    candidate = getCoord(point, -1, +1)
    if (candidate in black): nghb+=1
    candidate = getCoord(point, +1, +1)
    if (candidate in black): nghb+=1

    return nghb


def getNeigs4Plus(black, point):
# -
#-o-
# -
    nghb =0
    candidate=getCoord(point,-1,0)
    if (candidate in black): nghb-=1
    candidate = getCoord(point, +1, 0)
    if (candidate in black): nghb-=1
    candidate = getCoord(point, 0, -1)
    if (candidate in black): nghb-=1
    candidate = getCoord(point, 0, +1)
    if (candidate in black): nghb-=1


    candidate = getCoord(point, -1, -1)
    if (candidate in black): nghb -= 1
    candidate = getCoord(point, +1, -1)
    if (candidate in black): nghb -= 1
    candidate = getCoord(point, -1, +1)
    if (candidate in black): nghb -= 1
    candidate = getCoord(point, +1, +1)
    if (candidate in black): nghb -= 1


    candidate = getCoord(point, -2, +2)
    if (candidate in black): nghb -= 1
    candidate = getCoord(point, -2, +1)
    if (candidate in black): nghb -= 1
    candidate = getCoord(point, -2, 0)
    if (candidate in black): nghb -= 1
    candidate = getCoord(point, -2, -1)
    if (candidate in black): nghb -= 1
    candidate = getCoord(point, -2, -2)
    if (candidate in black): nghb -= 1
    candidate = getCoord(point, -1, -2)
    if (candidate in black): nghb -= 1
    candidate = getCoord(point, 0, -2)
    if (candidate in black): nghb -= 1
    candidate = getCoord(point, +1, -2)
    if (candidate in black): nghb -= 1

    candidate = getCoord(point, +2, -2)
    if (candidate in black): nghb += 1
    candidate = getCoord(point, +2, -1)
    if (candidate in black): nghb += 1
    candidate = getCoord(point, +2, 0)
    if (candidate in black): nghb += 1

    candidate = getCoord(point, +2, +1)
    if (candidate in black): nghb += 1
    candidate = getCoord(point, +2, +2)
    if (candidate in black): nghb += 1
    candidate = getCoord(point, +1, +2)
    if (candidate in black): nghb += 1
    candidate = getCoord(point, 0, +2)
    if (candidate in black): nghb += 1
    candidate = getCoord(point, -1, +2)
    if (candidate in black): nghb += 1



    return nghb

def getNeighbors2_1(black, point):
    nghb = 0
    candidate = getCoord(point, 0, -1)
    if (candidate in black): nghb+=1
    candidate = getCoord(point, 0, +1)
    if (candidate in black): nghb+=1
    return nghb
# +
# o
# +



def getEnergy(black):
    res=0
    i=0
    for point in black:
        i+=1
        res+=getNeigs(set(black),point) ##################              NEIGS
        if(i%report==0): print(100*i/len(black),"% culc E....",res)
    return res


def getNextState(black,curEnergy):
    for b in black:
        if(random.random()>0.8):
            black.remove(b)
            dx=int(size*(random.random()))
            if(random.random()>0.5): dx=-dx
            dy=int(size*(random.random()))
            if(random.random()>0.5): dy=-dy
            newB = getCoord(b, dx, dy)
            E=curEnergy-2*getNeigs(black,b)+2*getNeigs(black,newB)
            if(newB not in black and curEnergy>E):
                black.add(newB)
                #print("changed state: ",b,"->",newB,"| | energy: ",curEnergy,"->",E)
                curEnergy=E
            else: black.add(b)
    return list(black), curEnergy


def getCoord(point,dx,dy):
    if(point[0]+dx<0): x=size-1
    else:
        if(point[0]+dx >= size): x=0
        else: x=point[0]+dx
    if(point[1]+dy<0): y=size-1
    else:
        if(point[1]+dy >= size): y=0
        else: y=point[1]+dy
    return (x,y)



def getTemp(t,i):
    #return t*0.1/i
    if(i<400 and t<100): return 100
    #return t*0.99
    #return t**0.97
    return t*np.exp(-1/t)


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

def getStartIm(size,density):
    black=[]
    for i in range(size):
        for j in range(size):
            if(random.random()<=density): black.append((i,j))
    return black




def annealing(curState,t,endT,itr):
    i = 1
    curEnergy=0
    print("First E=",curEnergy)
    bestState=curState
    bestEnergy=curEnergy
    energies = []
    temp=[]
    start=time.time()
    while(i<itr or t>endT):
        nextState, nextEnergy=getNextState(set(curState),curEnergy)
        temp.append([i, t])
        if (bestEnergy > curEnergy):
            bestState = curState
            bestEnergy = curEnergy

        if(nextEnergy<curEnergy):
            energies.append([i, curEnergy])
            curEnergy=nextEnergy
            curState=nextState
        else:
            if(transition(nextEnergy-curEnergy,t)):
                energies.append([i, curEnergy])
                curEnergy=nextEnergy
                curState=nextState
        if(t>endT):
            t=getTemp(t,i)
        if(i%report==0):
            print("TIME: ",time.time()-start," E: ",curEnergy,"(",bestEnergy,")"," TEMP: ",t,"  ITR: ",i,"/",itr)
            start=time.time()
        i+=1
    plot(np.array(temp), 'red', False)
    plot(np.array(energies),'blue',False)
    showIm(size, bestState)
    print("E=",bestEnergy)
    print(bestState)


main()
print("TIME: ",time.time()-startAll)