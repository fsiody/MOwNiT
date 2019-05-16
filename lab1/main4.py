import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as clr

class Spot:

    def __init__(self):
        self.x=-1
        self.f = 0
        self.n=-1

    def __init__(self,x,f,n):
        self.x=x
        self.f=f
        self.n=n

def appendSpot(a,n):
    for i in range(len(spots)):
        s=spots[i]
        if np.isclose(s.x,a,rtol=1e-3,atol=0.0):
            s.f+=1
            s.n=n
            spots[i]=s
            return
    s=Spot(a,1,n)
    spots.append(s)

maxN=500

def foo(x0,r,n):
    max=maxN
    if n==0 :
        s=Spot(x0,1,n)
        spots.append(s)
        return foo(x0,r,n+1)
    if n<max:
        for i in range(len(spots)):
            if spots[i].n==n-1:
                x=spots[i].x
                a = r * x - r * x * x
                appendSpot(a,n)
        return foo(x0, r, n + 1)
    else:
        return max

_, ax = plt.subplots()
x0 = np.float32(0.3)
rMin=np.float32(0.0)
r=rMin
rMax=np.float32(4.0)
step=np.float32(0.05)
while(r<=4.0):
    spots=[]
    rs=[]
    xs=[]
    cl=[]
    foo(x0,r,0)
    for i in range(len(spots)):
        s=spots[i]
        if(s.f>5):
            xs.append(s.x)
            rs.append(r)
            cl.append(r)
    ax.scatter(rs,xs,vmin=int(rMin),vmax=int(rMax),s=5,marker=".",c=cl)
    r+=step
plt.title('x0=' + str(x0))
plt.xlabel('r')
plt.ylabel('x')
plt.show()