import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import integrate
import sys


class MWPC:
    def __init__(self,a,b):
        self.spessore = a  
        self.n_p = b
    def passaggio_particella(self):
       coppie_primarie = np.random.poisson(lam=self.n_p)
       posizioni=np.random.uniform(-self.spessore/2, self.spessore/2, size=coppie_primarie)
       return coppie_primarie,posizioni
    def sim_diffu(self,su,sf,nr,pos,tc):
        tmpy = pos
        #pos sono generati da posizioni in passaggio_particella
        tmpx = 0
        numero_passi=0
        while np.abs(tmpy) > 0.01:
            assorbimento= np.random.randint(0, high=nr,dtype=int)
            if assorbimento == 0:
                print('Elettrone è stato riassorbito!!!')
                break
            else:
                
                angolo=np.random.uniform(low=0,high=2*np.pi)
                tmpx = tmpx+su*np.cos(angolo)
                if tmpy > 0:
                    tmpy=tmpy+su*np.sin(angolo) - sf
                else:
                    tmpy=tmpy+su*np.sin(angolo) + sf
                numero_passi= numero_passi+1
                assorbimento = 1
        #calcolo tempo di deriva
        td = tc* numero_passi
        return td,assorbimento

#parametri di prova
n_p = 5
su = 10**(-4)
sf = 5 * 10**(-5)
nr=10**4
tc=10**(-12)

spessore=1

camera=MWPC(spessore,n_p)

passaggio_particella_prova=camera.passaggio_particella()

posizione_primo_elettrone_prova=passaggio_particella_prova[1][0]

tempo_der=camera.sim_diffu(su,sf,nr,posizione_primo_elettrone_prova,tc)
print('Il tempo di deriva per il primo elettrone è: ',tempo_der)


class eventi:
    def __init__(self,a,b,c,d):
        self.coppie_gen = a  
        self.cariche = b
        self.t_deriva = c
        self.pos_iniziale = d

# Implementare un script python che utilizzi le classi sopra descritte per:  
# simulare un numero congruo di particelle che attraversano la camera

spessore=1

camera=MWPC(spessore,n_p)

n_particelle = 3

tempi_di_deriva=[]

coppie_generate=[]

for i in range(0,n_particelle):
    camera.passaggio_particella()
    passaggio_particella=camera.passaggio_particella()
    posizioni=passaggio_particella[1]
    for i in posizioni:
        tempi_di_deriva.append(camera.sim_diffu(su,sf,nr,i,tc))
    coppie_generate.append(passaggio_particella[0])

