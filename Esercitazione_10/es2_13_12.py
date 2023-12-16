import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import integrate
import sys

sys.path.append('/Users/enricoduca/Documents/Università/MCF/Rep/Esercitazione_10/es1_13_12.py')
import es1_13_12
from es1_13_12 import random_walk2d_asimmetrica
from es1_13_12 import random_walk2d_asimmetrica2a

def p(phi):
    return 0.25*np.sin(phi/2)

def C(phi):
    return -0.5*(np.cos(phi/2)-1)

def invC(phi):
    return 2*np.arccos(-2*phi+1)

valori_prova = np.random.random(10)
print(invC(valori_prova))


# numero di valori estartti per generare la distribuzione
nsample = 100000

# valori y distribuiti uniformemnte in )0-1)
yrndq = np.random.random(nsample)

# valori x da cumulativa inversa
xrndq = invC(yrndq)

#fig, ax = plt.subplots(1,2, figsize=(11,5))

xq = np.arange(0, 2*np.pi, 0.01)
# y funzione onda quadro
yq = C(xq)

# grafico inversa cumulativa della funzione onda quadra nell'intervallo (0,5)
yc  = np.arange(0, 1, 0.001)
xc  = invC(yc)

print(xc)

fig,ax = plt.subplots(2,2, figsize=(11,7))#, sharex=True)#, sharey=True)
# grafico inversa cumulativa della funzione onda quadra nell'intervallo (0,5)
ax[1,0].plot(C(xq), xq, '--', linewidth=0.5, color='cornflowerblue')
ax[1,0].plot(yc, xc, linewidth=4, color='darkcyan')

#ax[1][0].grid()

ax[1,0].set_xlabel('y')
ax[1,0].set_ylabel(r'$c^{-1}$(y)')

ax[0,0].hist(yrndq, bins=100, color='cyan',   ec='darkcyan')
ax[0,0].set_title('Distribuzione y Cumulativa')
#ax[0,0].set_xlabel('y cumulativa')

#rot = transforms.Affine2D().rotate_deg(90)
ax[1,1].hist(xrndq, bins=100, color='orange', ec='darkorange', orientation=u'horizontal')
ax[1,1].set_title('Distribuzione secondo la funzione ')
#ax[1,1].set_ylabel('x')

ax[0, 1].axis('off')

plt.show()


# Modificare lo script python in modo tale che, attraverso la funzione per la diffusione asimmetrica appena definita, produca un grafico 2D delle posizioni di 5 random walker per 1000 passi.

lista_array_x = []
lista_array_y = []
s=1
N=1000

distanzex=[]
distanzey=[]
distanza_tot=[]

for i in range(5):
    distanza_x = random_walk2d_asimmetrica(s,N)[0]
    distanza_y = random_walk2d_asimmetrica(s,N)[1]
    distanzex.append(distanza_x)
    distanzey.append(distanza_y)
    distanza_tot.append(distanza_x**2+distanza_y**2)

for i in range(5):
    plt.plot(distanzex[i],distanzey[i],label='Random walker {:}'.format(i))
plt.title('Grafico 2D delle posizioni di 5 random walker per 1000 passi')
plt.legend()
plt.show()

#Modificare lo script python in modo tale che, attraverso la funzione per la diffusione asimmetrica 
# appena definita, produca un grafico 2D delle posizioni di 5 walker per: s_f=0.1 e per s_f=0.01

posizioni = random_walk2d_asimmetrica2a(0.1, 0.1)

for (x, y) in (posizioni[:100000]):
                print(f" X={x}, Y={y}")

x, y = zip(*posizioni)
plt.plot(x, y)
plt.title('2D Random Walk fino a x = 0.1*200')
plt.xlabel('coordinate x')
plt.ylabel('coordinate y')
plt.show()

posizioni2 = random_walk2d_asimmetrica2a(0.01, 0.01)

for (x, y) in (posizioni2[:100000]):
                print(f" X={x}, Y={y}")

x, y = zip(*posizioni2)
plt.plot(x, y)
plt.title('2D Random Walk fino a x = 0.01*200')
plt.xlabel('coordinate x')
plt.ylabel('coordinate y')
plt.show()