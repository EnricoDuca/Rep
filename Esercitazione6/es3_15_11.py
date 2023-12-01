import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import array as arr

file=pd.read_csv('/Users/enricoduca/Documents/Università/MCF/get-mcf-data/oscilloscope.csv')

print(file)

print(file.columns)

tempo=np.asarray(file['time'])
signal1=np.asarray(file['signal1'])
signal2=np.asarray(file['signal2'])

plt.plot(tempo,signal1)
plt.xlabel('Tempo')
plt.ylabel('Segnale 1')
plt.show()
plt.plot(tempo,signal2)
plt.xlabel('Tempo')
plt.ylabel('Segnale 2')
plt.show()

#calcolo la derivata del segnale attraverso la differenza centrale;

def derivata(t,s):
    arr=[]
    for i in range(0,len(s)-2):
        num=s[i+2]-s[i]
        den=t[i+2]-t[i]
        arr.append(num/den)
    return arr

plt.plot(tempo[:-2],derivata(tempo,signal1))
plt.xlabel('Tempo')
plt.ylabel('Derivata Segnale 1')
plt.show()

plt.plot(tempo[:-2],derivata(tempo,signal2))
plt.xlabel('Tempo')
plt.ylabel('Derivata Segnale 2')
plt.show()

#calcolo derivata con numpy.gradient

npgrad_sig1 = np.gradient(signal1,tempo)
plt.plot(tempo,npgrad_sig1)
plt.xlabel('Tempo')
plt.ylabel('Segnale 1 con numpy.gradient')
plt.show()

npgrad_sig2 = np.gradient(signal1,tempo)
plt.plot(tempo,npgrad_sig2)
plt.xlabel('Tempo')
plt.ylabel('Segnale 2 con numpy.gradient')
plt.show()

#calcolo derivata con n

print(len(tempo),len(signal1))

def derivata_n(t, s, nh):
    dd = s[nh:] - s[:-nh]
    hh = t[nh:] - t[:-nh]
    
    for ih in range(int(nh/2)):
        dd = np.append(s[nh-ih-1]-s[0], dd)
        dd = np.append(dd, s[len(s)-1]-s[len(s)-(nh-ih)])
    
        hh = np.append(t[nh-ih-1]-t[0], hh)
        hh = np.append(hh, t[len(t)-1]-t[len(t)-(nh-ih)])
    
    return dd/hh

plt.plot(tempo,derivata_n(tempo,signal1,100))
plt.xlabel('Tempo')
plt.ylabel('Derivata con distanze n ')
plt.show()
