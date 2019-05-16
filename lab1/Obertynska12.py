import time
import numpy as np
import matplotlib.pyplot as plt
#from pylab import *


n=10000000
v=0.3

suma=v*n
print("sum = ", suma)
print()
def getSum1(v, n):
    startTimeSum=time.time()
    sum1=0
    _, ax = plt.subplots()
    iArray=[]
    eArray=[]
    for i in range(1, n):
        sum1+=v
        if (i%2500==0 or i==n or i==n-1):
            aeP = abs(sum1 - i*v)
            reP = aeP / (i*v)
            eArray.append(reP)
            iArray.append(i)
    ax.plot(iArray,eArray)
    print("sumSum = ", sum1)
    ae1=abs(sum1-suma)
    re1=ae1/suma
    print("aeSum = ", ae1)
    print("reSum = ", re1)
    print("timeSum = ", time.time()-startTimeSum)
    return sum1

def getSum2(v, n):
    startTimeRek=time.time()
    sum2=getSum2rek(v,n)
    rekTime=time.time()-startTimeRek
   # sum2=0
    print()
    print("sumRek = ", sum2)
    ae2 = abs(sum2 - suma)
    re2 = ae2 / suma
    print("aeRek = ", ae2)
    print("reRek = ", re2)
    print("timeRek = ", rekTime)
    return sum2


def getSum2rek(v,n):

    if n==0: return 0
    if n==1: return v
    else:
        if n%2==1:
            return v + getSum2rek(v + v, n // 2)
        else:
            return getSum2rek(v+v,n/2)


def getSumKahan(v,n):
    startTimeK = time.time()
    sumK=0
    err=0
    for i in range(1,n+1):
        y=v-err
        temp=sumK+y
        err=(temp-sumK)-y
        sumK=temp
    print()
    kTime = time.time() - startTimeK
    print("sumK = ",sumK)
    aeK = abs(sumK - suma)
    reK = aeK / suma
    print("aeK = ", aeK)
    print("reK = ", reK)
    print("timeK = ", kTime)




getSum1(v,n)
getSum2(v,n)
getSumKahan(v,n)
plt.show()



