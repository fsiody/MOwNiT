import numpy as np
import math
import cmath

def getEps(n,j,pow):
    return complex(math.cos(2*math.pi*j*pow/n),(math.sin(2*math.pi*j*pow/n)))



n=8
F=np.zeros((n,n),dtype=complex)
for i in range(n):
    for j in range(n):
        F[i,j]=getEps(n,i,j)
y=np.array([1,2,3,4,5,6,7,8],dtype=complex)

print(F)

m=int(n/2)
E=np.zeros((m,m),dtype=complex)
for i in range(m):
    for j in range(m):
        E[i,j]=getEps(m,i,j)

A=np.zeros((m,m),dtype=complex)
for i in range(m):
    for j in range(m):
        A[i,j]=F[i,2*j]
print()
print()
print(A)


B=np.zeros((m,m),dtype=complex)
for i in range(m):
    for j in range(m):
        B[i,j]=F[i,2*j+1]
print()
print()
print(B)

C=np.zeros((m,m),dtype=complex)
for i in range(m):
    for j in range(m):
        C[i,j]=F[m+i,2*j]
print()
print()
print(C)

D=np.zeros((m,m),dtype=complex)
for i in range(m):
    for j in range(m):
        D[i,j]=F[m+i,2*j+1]
print()
print()
print(D)