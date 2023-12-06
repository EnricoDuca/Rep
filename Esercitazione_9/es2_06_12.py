import scipy 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import fft, constants
from scipy.fft import ifft, rfft, irfft, fft,rfftfreq
from scipy import optimize
from scipy.optimize import curve_fit

#Leggere i file di dati e generare un DataFrame pandas per ciascuno di essi;

file1=pd.read_csv('/Users/enricoduca/Documents/Università/MCF/get-mcf-data/4FGL_J0428.6-3756_weekly_9_15_2023_mcf.csv')
file2=pd.read_csv('/Users/enricoduca/Documents/Università/MCF/get-mcf-data/4FGL_J0721.9+7120_weekly_9_15_2023_mcf.csv')
file3=pd.read_csv('/Users/enricoduca/Documents/Università/MCF/get-mcf-data/4FGL_J1256.1-0547_weekly_9_15_2023_mcf.csv')
file4=pd.read_csv('/Users/enricoduca/Documents/Università/MCF/get-mcf-data/4FGL_J2202.7+4216_weekly_9_15_2023_mcf.csv')
file5=pd.read_csv('/Users/enricoduca/Documents/Università/MCF/get-mcf-data/4FGL_J2232.6+1143_weekly_9_15_2023_mcf.csv')
file6=pd.read_csv('/Users/enricoduca/Documents/Università/MCF/get-mcf-data/4FGL_J2253.9+1609_weekly_9_15_2023_mcf.csv')
giorno_giuliano=file1['Julian Date']

#Generare un grafico di tutte le curve di luce (Flusso vs Giorno Giuliano) sovrapposte con una legenda che identifichi le sorgenti;

plt.figure(figsize=(10,7))
plt.plot(file1['Julian Date'],file1['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'],c='red',label='sorgente PKS 0426-380, classe BLL')
plt.plot(file2['Julian Date'],file2['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'],c='green',label='sorgente S5 0716+71, classe BLL')
plt.plot(file3['Julian Date'],file3['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'],c='gold',label='sorgente 3C 279, classe FSRQ')
plt.plot(file4['Julian Date'],file4['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'],c='grey',label='sorgente BI Lac, classe BLL')
plt.plot(file5['Julian Date'],file5['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'],c='purple',label='sorgente CTA 102, classe FSRQ')
plt.plot(file6['Julian Date'],file6['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'],c='blue',label='sorgente 3C 454.3, classe FSRQ')

plt.xlabel('Giorno giuliano')
plt.ylabel('Flusso di fotoni (cm-2 s-1)')
plt.legend()
plt.show()

#Generare un unico grafico con 6 pannelli sovrapposti, in ogni pannello deve comparire la curva di luce di una sorgente;

fig,ax=plt.subplots(3,2,figsize=(10,7))

ax[2][1].plot(file1['Julian Date'],file1['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'],c='limegreen',label='sorgente PKS 0426-380, classe BLL')
ax[0][1].plot(file2['Julian Date'],file2['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'],c='limegreen',label='sorgente S5 0716+71, classe BLL')
ax[1][0].plot(file3['Julian Date'],file3['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'],c='deepskyblue',label='sorgente 3C 279, classe FSRQ')
ax[1][1].plot(file4['Julian Date'],file4['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'],c='limegreen',label='sorgente BI Lac, classe BLL')
ax[2][0].plot(file5['Julian Date'],file5['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'],c='deepskyblue',label='sorgente CTA 102, classe FSRQ')
ax[0][0].plot(file6['Julian Date'],file6['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'],c='deepskyblue',label='sorgente 3C 454.3, classe FSRQ')

ax[0][0].set_title('Curve di Luce FSRQ')
ax[0][1].set_title('Curve di Luce BLL')

ax[2][0].set_xlabel('Giorno giuliano')
ax[2][1].set_xlabel('Giorno giuliano')

for i in range(0,3):
    for j in range(0,2):
        ax[i][j].legend(loc='upper right')

plt.show()

# Calcolare la trasformata di Fourier delle curve di luce

fft1=rfft(file1['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'].values)
fft2=rfft(file2['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'].values)
fft3=rfft(file3['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'].values)
fft4=rfft(file4['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'].values)
fft5=rfft(file5['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'].values)
fft6=rfft(file6['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'].values)

# Generare un grafico con gli spettri di potenza delle diverse sorgenti sovrapposti

dt=giorno_giuliano[3] - giorno_giuliano[2]

fftfreq1=0.5*rfftfreq(len(fft1),d=dt)
fftfreq2=0.5*rfftfreq(len(fft2),d=dt)
fftfreq3=0.5*rfftfreq(len(fft3),d=dt)
fftfreq4=0.5*rfftfreq(len(fft4),d=dt)
fftfreq5=0.5*rfftfreq(len(fft5),d=dt)
fftfreq6=0.5*rfftfreq(len(fft6),d=dt)

potenza1=np.abs(fft1[:len(fft1)//2])**2
potenza2=np.abs(fft2[:len(fft2)//2])**2
potenza3=np.abs(fft3[:len(fft3)//2])**2
potenza4=np.abs(fft4[:len(fft4)//2])**2
potenza5=np.abs(fft5[:len(fft5)//2])**2
potenza6=np.abs(fft6[:len(fft6)//2])**2

plt.plot(fftfreq1[:-1],potenza1,c='limegreen',label='classe BLL')
plt.plot(fftfreq2[:-1],potenza2,c='limegreen')
plt.plot(fftfreq3[:-1],potenza3,c='deepskyblue',label='classe FSRQ')
plt.plot(fftfreq4[:-1],potenza4,c='limegreen')
plt.plot(fftfreq5[:-1],potenza5,c='deepskyblue')
plt.plot(fftfreq6[:-1],potenza6,c='deepskyblue')
plt.yscale('log')
plt.xscale('log')
plt.xlabel('Frequenze (Hz)')
plt.title('Spettri di potenza -scala logaritmica-')
plt.legend(loc='upper right')
plt.show()

# Generare un grafico con gli spettri di potenza delle diverse sorgenti sovrapposti e normalizzati ai rispettivi coefficiente di ordine zero

potenza1_norm=np.abs(fft1[:len(fft1)//2])**2/potenza1[0]
potenza2_norm=np.abs(fft2[:len(fft2)//2])**2/potenza2[0]
potenza3_norm=np.abs(fft3[:len(fft3)//2])**2/potenza3[0]
potenza4_norm=np.abs(fft4[:len(fft4)//2])**2/potenza4[0]
potenza5_norm=np.abs(fft5[:len(fft5)//2])**2/potenza5[0]
potenza6_norm=np.abs(fft6[:len(fft6)//2])**2/potenza6[0]

plt.plot(fftfreq1[:-1],potenza1_norm,c='limegreen',label='classe BLL')
plt.plot(fftfreq2[:-1],potenza2_norm,c='limegreen')
plt.plot(fftfreq3[:-1],potenza3_norm,c='deepskyblue',label='classe FSRQ')
plt.plot(fftfreq4[:-1],potenza4_norm,c='limegreen')
plt.plot(fftfreq5[:-1],potenza5_norm,c='deepskyblue')
plt.plot(fftfreq6[:-1],potenza6_norm,c='deepskyblue')
plt.yscale('log')
plt.xscale('log')
plt.xlabel('Frequenze (u.a.)')
plt.title('Spettri di potenze normalizzate -scala logaritmica-')
plt.legend(loc='upper right')
plt.show()