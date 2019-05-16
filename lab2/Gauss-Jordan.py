import numpy as np
import time

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

def getZerosColumn(a,n,k):
    for i in range(k+1,n):
        tmp=a[i][k]
        for j in range(k,n+1):
            a[i][j]+=-a[k][j]*tmp

def matrixSolution(a,n):
    for i in range(0,n):
        columnPermutation(a,n,i)
        getZerosColumn(a,n,i)




min=-500.0
max=500.0
n=750
A=np.random.uniform(min,max,(n,n+1))

Anp=[]
Bnp=[]
for i in range(n):
    Anp.append([])
    Bnp.append(A[i][n])
    for j in range(n):
        Anp[i].append(A[i][j])

#for i in range(n): print(Anp[i], "   |   ",Bnp[i])

#start lib fun
stnp=time.time()
Xnp=np.linalg.solve(Anp,Bnp)
endnp=time.time()-stnp
print("\n Np solution in time ",endnp)
print(Xnp)
print()


#start my fun
X=[]
st=time.time()
for i in range(n): X.append(i)
for i in range(n):
    scaling(A,i,n)
    columnPermutation(A,n,i,i)
    getZerosColumn(A,n,i)

sol=[]
for i in  range(n): sol.append(0)
for i in range(n):
    j=n-i-1
    s=A[j][n]
    for k in range(n):
        s-=A[j][k]*sol[X[k]]
    sol[X[j]]=s

end=time.time()-st
print("\n My solution in time ",end)
print(sol)
