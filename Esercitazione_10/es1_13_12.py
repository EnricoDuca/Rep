import sys
import numpy as np
import scipy 
import matplotlib.pyplot as plt
from matplotlib import  transforms

#Produrre un modulo python che definisca una procedura di Random Walk in due dimensioni con le seguenti caratteristiche
#La diffusione ha un passo costante di lunghezza ;
#ad ogni passo lo spostamento può andare con uguale probabilità in ogni direzione (probabilità costante per psi appartentne a (0,2pi(.

#phi=np.arange(0,2*np.pi,0.1)

def random_walk2d(step,N):
    
    deltax = np.array([0])
    deltay= np.array([0])
    tmpx = 0
    tmpy = 0
    check = np.random.uniform(low=0,high=2*np.pi, size=N)
    for i in check:
            tmpx = tmpx+step*np.cos(i)
            tmpy=tmpy+step*np.sin(i)
            deltax = np.append(deltax, tmpx)
            deltay=np.append(deltay,tmpy)
    return deltax,deltay

def random_walk2d_asimmetrica(step,N):
    deltax = np.array([0])
    deltay= np.array([0])
    tmpx = 0
    tmpy = 0
    check = 2*np.arccos(-2*(np.random.random(N))+1)
    for i in check:
            tmpx = tmpx+step*np.cos(i)
            tmpy=tmpy+step*np.sin(i)
            deltax = np.append(deltax, tmpx)
            deltay=np.append(deltay,tmpy)
    return deltax,deltay

#Modificare il modulo python per la diffusione 2D aggiungendo una funzione analoga a quella simmetrica ma 
# aggiungendo ad ogni passo un contributo costante e positivo s_f 
# lungo l'asse x, invece di stabilire a priori il numero di passi, arrestare il processo quando 
# la coordinata xsupera un valore prestabilito

def random_walk2d_simmetrica2a(step,s_f):
    deltax = [0]
    deltay = [0]
    tmpx = 0
    tmpy = 0
    check = np.random.uniform(low=0,high=2*np.pi, size=10000000)
    for i in check:
        if np.abs(tmpx) < 200*step:
                tmpx = tmpx + (step * np.cos(i) + s_f)
                tmpy = tmpy + step * np.sin(i)
                deltax.append(tmpx)
                deltay.append(tmpy)
        else:
             break
    return list(zip(deltax, deltay))

# con il ciclo while è meglio perchè non so a priori il numero di passi
# def random_walk2d(step,sf):
    
#     deltax = np.array([0])
#     deltay= np.array([0])
#     tmpx = 0
#     tmpy = 0
#     numero_passi=0
#     while tmpy < 200*step:
#             check = np.random.uniform(low=0,high=2*np.pi)
#             if tmpy<0:
#                     tmpx = tmpx+step*np.cos(check)
#                     tmpy=tmpy+step*np.sin(check) - sf
#                     deltax = np.append(deltax, tmpx)
#                     deltay=np.append(deltay,tmpy)
#                     numero_passi = numero_passi+1
#             if tmpy>0:
#                     tmpx = tmpx+step*np.cos(check)
#                     tmpy=tmpy+step*np.sin(check) + sf
#                     deltax = np.append(deltax, tmpx)
#                     deltay=np.append(deltay,tmpy)
#                     numero_passi = numero_passi+1
#     return deltax,deltay,numero_passi
