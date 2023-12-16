import sys
import numpy as np
import scipy 
import matplotlib.pyplot as plt
from matplotlib import  transforms

# Definire uno script python che importi il modulo precedentemente definito per:

# produrre un grafico 2D delle posizioni di 5 random walker per 1000 passi 

sys.path.append('/Users/enricoduca/Documents/Università/MCF/Rep/Esercitazione_10/es1_13_12.py')
import es1_13_12
from es1_13_12 import random_walk2d

lista_array_x = []
lista_array_y = []
s=1
N=1000

distanzex=[]
distanzey=[]
distanza_tot=[]

for i in range(5):
    distanza_x = random_walk2d(s,N)[0]
    distanza_y = random_walk2d(s,N)[1]
    distanzex.append(distanza_x)
    distanzey.append(distanza_y)
    distanza_tot.append(distanza_x**2+distanza_y**2)

for i in range(5):
    plt.plot(distanzex[i],distanzey[i],label='Random walker {:}'.format(i))
plt.title('Grafico 2D delle posizioni di 5 random walker per 1000 passi')
plt.show()

#produrre un grafico 2D della posizione di 100 random walker dopo 10, 100 e 1000 passi;

list_passi=[10,100,1000]
distanza10_x=[]
distanza10_y=[]
distanza100_x=[]
distanza100_y=[]
distanza1000_x=[]
distanza1000_y=[]

for p in list_passi:
    if (p == 10):
        for i in range(100):
            distanza10_x.append(random_walk2d(s,p)[0])
            distanza10_y.append(random_walk2d(s,p)[1])
    if (p == 100):
        for i in range(100):
            distanza100_x.append(random_walk2d(s,p)[0])
            distanza100_y.append(random_walk2d(s,p)[1])
    if (p == 1000):
        for i in range(100):
            distanza1000_x.append(random_walk2d(s,p)[0])
            distanza1000_y.append(random_walk2d(s,p)[1])

fig,ax=plt.subplots(3,1,sharex=True,figsize=(8,7))

ax[0].plot(distanza10_x,distanza10_y ,c='royalblue')
ax[1].plot(distanza100_x,distanza100_y, c='darkred')
ax[2].plot(distanza1000_x,distanza1000_y, c='sandybrown')
ax[0].set_title('100 Random walker con 10 passi')
ax[1].set_title('100 Random walker con 100 passi')
ax[2].set_title('100 Random walker con 1000 passi')
plt.show()

#produrre ung grafico con due pannelli che mosti:
    # nel primo pannello lo stesso grafico del punto A;
    # nel secondo pannello il quadrato della distanza dal punto di partenza in funzione dei passi per gli stessi 5 random walker.

passi=np.arange(1001)

fig,ax=plt.subplots(1,2,figsize=(11,7))

for i in range(5):
    ax[0].plot(distanzex[i],distanzey[i],label='Random walker {:}'.format(i))

for i in range(5):
    ax[1].plot(passi,distanza_tot[i],label='Random walker {:}'.format(i))

ax[0].set_title('Grafico 2D delle posizioni di 5 random walker per 1000 passi')
ax[1].set_title('Quadrato della distanza dal punto di partenza')
ax[1].set_xlabel('passi')
ax[0].legend()
ax[1].legend()
plt.show()
