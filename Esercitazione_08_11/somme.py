import numpy as np
import matplotlib.pyplot as plt

def somma(n):
    s=0
    for i in range(0,n+1):
        s=s+i
    return s

def somma_radici(n):
    s=0
    for i in range(0,n+1):
        s=s+np.sqrt(i)
    return s

def somma_prodotto(n):
    s=0
    p=1
    for i in range(1,n+1):
        s=s+i
        p=p*i   
    return s,p

def sommatoria(n,alfa=1):
    s=0
    for i in range (1,n+1):
        s=s+(i**alfa)
    return s