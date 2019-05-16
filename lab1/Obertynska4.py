import matplotlib.pyplot as plt
import numpy as np

nMax=200

def foo(x0,r,n):
    if n==0 :
        a=r*x0-r*x0*x0
        n+=1
    while n<nMax:
        a = r * a - r * a * a
        n+=1
        if(n>nMax-10):
            xs.append(a)


_, ax = plt.subplots()
x0 = np.float32(0.2)
r=rMin=np.float32(1.0)
rMax=np.float32(5.0)
step=np.float32(0.005)
while(r<=rMax):
    rs=[]
    xs=[]
    foo(x0,r,0)
    for i in range(len(xs)):
        rs.append(r)
    ax.scatter(rs,xs,s=0.5,vmin=int(rMin),vmax=int(20),marker=".",c=rs)
    r+=step
plt.title('pojedyncza precyzja x0=' + str(x0))
plt.xlabel('r')
plt.ylabel('x')
plt.show()