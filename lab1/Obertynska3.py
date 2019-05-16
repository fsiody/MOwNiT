import time
import numpy as np
import matplotlib.pyplot as plt

s = 2;      n = 50
s = 3.6667; n = 100
s = 5;      n = 200
s = 7.2;    n = 500
s = 10;     n = 1000

print("s = ",s,"    n = ",n)
def dzetaR32(s, start, end):
    sumDzetaR32 = np.float32(0.0)
    step = 1
    if start > end:
        step = -1
    while start != end:
        sumDzetaR32 += 1 / (start ** s)
        start += step
    sumDzetaR32+=1 / (start ** s)
    return sumDzetaR32



def dzetaR64(s, start, end):
    sumDzetaR64 = np.float64(0.0)
    step = 1
    if start > end:
        step = -1
    while start != end:
        sumDzetaR64 += 1 / (start ** s)
        start += step
    sumDzetaR64+=1 / (start ** s)
    return sumDzetaR64



a = dzetaR32(np.float32(s), 1, n)
b = dzetaR32(np.float32(s), n, 1)
print("dzeta Riemana 32:")
print("sumowanie w przud ", a)
print("sumowanie wstecz  ", b)
print("roznica           ", abs(a - b))
print()

a = dzetaR64(np.float64(s), 1, n)
b = dzetaR64(np.float64(s), n, 1)
print("dzeta Riemana 64:")
print("sumowanie w przud ", a)
print("sumowanie wstecz  ", b)
print("roznica           ", abs(a - b))
print()

def etaD32(s, start, end):
    sumEtaD32 = np.float32(0.0)
    step = 1
    if (start > end):
        step = -1
    while start != end:
        sumEtaD32 += ((-1) ** (start - 1)) / (start ** s)
        start += step
    sumEtaD32+=((-1) ** (start - 1)) / (start ** s)
    return sumEtaD32

def etaD64(s, start, end):
    sumEtaD64 = np.float64(0.0)
    step = 1
    if start > end:
        step = -1
    while start != end:
        sumEtaD64 += ((-1) ** (start - 1)) / (start ** s)
        start += step
    sumEtaD64 += ((-1) ** (start - 1)) / (start ** s)
    return sumEtaD64

print()

a = etaD32(np.float32(s), 1, n)
b = etaD32(np.float32(s), n, 1)
print("eta Dirichleta 32:")
print("sumowanie w przud ", a)
print("sumowanie wstecz  ", b)
print("roznica           ", abs(a - b))
print()


a = etaD64(np.float64(s), 1, n)
b = etaD64(np.float64(s), n, 1)
print("eta Dirichleta 64:")
print("sumowanie w przud ", a)
print("sumowanie wstecz  ", b)
print("roznica           ", abs(a - b))
print()

# plt.show()
