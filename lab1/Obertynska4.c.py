import numpy as np
import time

def foo(x0,r,n):
    if n==0 :
        a=x0
    while 1:
        if  np.isclose(a,np.float32(0.0),rtol=1e-6,atol=1e-6):
            print(a)
            return n
        a = r * a - r * a * a
        n+=1


x0 = np.float32(0.68)
r=np.float32(4.0)
start=time.time()
print(foo(x0,r,0))
print(time.time()-start)