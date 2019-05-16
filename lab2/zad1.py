import numpy as np
import copy

def scaling(a,start,n):
    for i in range(start,n):
        maxEl = 0.0
        for j in range(start,n):
            if abs(a[i][j])>abs(maxEl):
                maxEl=a[i][j]
        print(maxEl)
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
n=3
print(id)
A=np.random.uniform(min,max,(n,n+1))
#A=[[1,5,7],[3,-2,4]]
B=[]
for i in range(n):
    B.append([])
    for j in range(n+1):
        B[i].append(A[i][j])
X=[]
print("A origin")
for i in range(n):
    print(A[i])
    X.append(i)



for i in range(n):
    print(" ------------------------ ")
    print("|------------"+str(i)+"------------|")
    print(" ------------------------ ")
    scaling(A,i,n)
    print()
    print("A scalled")
    for j in range(n): print(A[j],"  |  ",X[j])

    print()
    print()
    print("permutation ")
    columnPermutation(A,n,i,i)
    for j in range(n): print(A[j], "  |  ", X[j])
    print()

    getZerosColumn(A,n,i)
    print("zeros column")
    for j in range(n): print(A[j], "  |  ", X[j])


sol=[]
for i in  range(n): sol.append(0)
for i in range(n):
    j=n-i-1
    s=A[j][n]
    for k in range(n):
        s-=A[j][k]*sol[X[k]]
    sol[X[j]]=s


print()
print("-----------")
print("SOLUTION")
print(sol)
print()
s=0
for i in range(n):
    print(B[i])
    s+=sol[i]*B[0][i]
print(s," = ", B[0][n])

for i in range(n): print(i)