import numpy as np
import time
import scipy.linalg

def scaling(a,start,n):
    for i in range(start,n):
        maxEl = 0.0
        for j in range(start,n):
            if abs(a[i][j])>abs(maxEl):
                maxEl=a[i][j]
        for j in range(start,n+1):
            a[i][j]/=maxEl


def swap(a,w,k1,k2):
    tmp=a[w][k1]
    a[w][k1]=a[w][k2]
    a[w][k2]=tmp



def columnPermutation(a,n,w,k):
    kJeden=k
    for i in range(k,n):
        if np.isclose(abs(a[w][i]),1.0,rtol=1.e-5,atol=1.e-5): kJeden=i
    for i in range(n):
        swap(a,i,k,kJeden)
    tmp=X[kJeden]
    X[kJeden]=X[k]
    X[k]=tmp

def getZerosColumnDown(a,n,k):
    for i in range(k+1,n):
        tmp=a[i][k]
        L[i][k]=tmp
        for j in range(k,n+1):
            a[i][j]+=-a[k][j]*tmp


min=-500.0
max=500.0
n=500
print(id)
A=np.random.uniform(min,max,(n,n+1))
B=[]
L=[]
Acopy=[]
for i in range(n):
    L.append([])
    Acopy.append([])
    for j in range(n):
        Acopy[i].append(A[i][j])
        L[i].append(0)
X=[]
#print("A origin")
for i in range(n):
    L[i][i]=1.0
  #  print(A[i])
    X.append(i)


startt=time.time()
for i in range(n):
    scaling(A,i,n)
    columnPermutation(A,n,i,i)
    getZerosColumnDown(A,n,i)
print("moj czas LU: ", time.time()-startt)
print("\n B@L")

startSci=time.time()
(Pnp,Lnp,Unp)=scipy.linalg.lu(Acopy)
print("lib czas lu: ",time.time()-startSci)