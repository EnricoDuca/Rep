import scipy 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import fft, constants
from scipy.fft import ifft, rfft,irfft
from scipy import optimize
from scipy.optimize import curve_fit

#leggere i tre file messi a disposizione;

file1=pd.read_csv('/Users/enricoduca/Documents/Università/MCF/get-mcf-data/data_sample1.csv')
file2=pd.read_csv('/Users/enricoduca/Documents/Università/MCF/get-mcf-data/data_sample2.csv')
file3=pd.read_csv('/Users/enricoduca/Documents/Università/MCF/get-mcf-data/data_sample3.csv')

# produco un grafico dei tre segnali di ingresso;

# print(file1)
# print(file1.columns)

x1=file1['time']
y1=file1['meas']
plt.plot(x1,y1, color='red')

x2=file2['time']
y2=file2['meas']
plt.plot(x2,y2, color='blue')

x3=file3['time']
y3=file3['meas']
plt.plot(x3,y3,color='green')

plt.xlabel('Time[s]')
plt.legend(['data_sample1', 'data_sample2', 'data_sample3'], loc='upper right')
plt.show()

fig,ax=plt.subplots(3,1,sharex=True)

ax[0].plot(x1,y1,c='red')
ax[1].plot(x2,y2, c='blue')
ax[2].plot(x3,y3, c='green')
plt.xlabel('Time[s]')
ax[0].set_ylabel('meas[u.a.]')
ax[0].set_title('data_sample1')
ax[1].set_ylabel('meas[u.a.]')
ax[1].set_title('data_sample2')
ax[2].set_ylabel('meas[u.a.]')
ax[2].set_title('data_sample3')
plt.show()

#Calcolare la trasformata di Fourier dei segnali di ingreso e produrre il grafico dello spettro di potenza;

dt=x1[1]-x1[0]

datafft1 = fft.rfft(y1.values)

fftfreq1 = 0.5*fft.rfftfreq(len(datafft1),d=dt)

datafft2 = fft.rfft(y2.values)

fftfreq2 = 0.5*fft.rfftfreq(len(datafft2),d=dt)

datafft3 = fft.rfft(y3.values)

fftfreq3 = 0.5*fft.rfftfreq(len(datafft3),d=dt)

potenza1 = np.abs(datafft1[:len(datafft1)//2])**2
potenza2 = np.abs(datafft2[:len(datafft2)//2])**2
potenza3 = np.abs(datafft3[:len(datafft3)//2])**2

fig,ax=plt.subplots(3,1,sharex=True)

ax[0].plot(fftfreq1[:len(datafft1)//2],potenza1,c='red')
ax[1].plot(fftfreq2[:len(datafft2)//2],potenza2, c='blue')
ax[2].plot(fftfreq3[:len(datafft3)//2],potenza3, c='green')
plt.xlabel('Time[s]')
ax[0].set_ylabel('potenza data_sample1')
ax[1].set_ylabel('potenza data_sample2')
ax[2].set_ylabel('potenza data_sample3')
plt.show()


potenza1_fit = np.abs(datafft1)**2
potenza2_fit = np.abs(datafft2)**2
potenza3_fit = np.abs(datafft3)**2

mask1 = potenza1_fit > 5e3
datafft1_filtrato = datafft1*mask1
y1_filtrato = fft.irfft(datafft1_filtrato)

mask1_2 = potenza1_fit > 10e3
datafft1_filtrato_2 = datafft1*mask1_2
y1_filtrato_2 = fft.irfft(datafft1_filtrato_2)

plt.plot(x1, y1_filtrato, label='iFFT - $|c_k|^2>5*10^3$',c='magenta')
plt.plot(x1, y1_filtrato_2, label='iFFT - $|c_k|^2>10^4$',c='limegreen')
plt.plot(x1, y1, label='Segnale originale',c='gold',alpha=0.35)
plt.legend()
plt.title('data_sample1')
plt.show()

mask2 = potenza2_fit > 100e3
datafft2_filtrato = datafft2*mask2
y2_filtrato = fft.irfft(datafft2_filtrato)

plt.plot(x2, y2_filtrato, label='iFFT - $|c_k|^2>10^5$',c='magenta')
plt.plot(x2, y2, label='Segnale originale',c='gold',alpha=0.35)
plt.legend()
plt.title('data_sample2')
plt.show()

mask3 = potenza3_fit > 0.1e6
datafft3_filtrato = datafft3*mask3
y3_filtrato = fft.irfft(datafft3_filtrato)

mask3_2 = potenza3_fit > 0.2e6
datafft3_filtrato_2 = datafft3*mask3_2
y3_filtrato_2 = fft.irfft(datafft3_filtrato_2)

plt.plot(x3, y3_filtrato, label='iFFT - $|c_k|^2>10^5$',c='magenta')
plt.plot(x3, y3_filtrato_2, label='iFFT - $|c_k|^2>0.2*10^6$',c='limegreen')
plt.plot(x3, y3, label='Segnale originale',c='gold')
plt.legend()
plt.title('data_sample3')
plt.show()

#Fare il fit dei tre spettri di potenza per determinarne l'andamento in funzione della frequenza e identifichi il tipo di rumore per ogni serie di dati.

mask0=fftfreq1[:len(datafft2)//2] != 0
mask0_2=fftfreq2[:len(datafft2)//2] != 0
mask0_3=fftfreq3[:len(datafft2)//2] != 0


def andamento(x,a,beta):
    return (a/x**beta)


params, params_covariance = curve_fit(andamento, xdata=fftfreq1[:len(datafft2)//2][mask0], ydata=potenza1[1:])
params_err=np.sqrt(np.diag(params_covariance))
plt.plot(fftfreq1[:len(datafft2)//2][mask0], andamento(fftfreq1[:len(datafft2)//2][mask0], params[0],params[1]), c='sandybrown', label='Fit')
plt.plot(fftfreq1[:len(datafft2)//2][mask0], potenza1[1:], label='Segnale originale',c='red',alpha=0.35)
plt.legend()
plt.yscale('log')
plt.xscale('log')
print('i parametri sono: ',params,' con errori: ',params_err)
plt.show()


params, params_covariance = curve_fit(andamento, xdata=fftfreq2[:len(datafft2)//2][mask0_2], ydata=potenza2[1:])
params_err=np.sqrt(np.diag(params_covariance))
plt.plot(fftfreq2[:len(datafft2)//2][mask0_2], andamento(fftfreq2[:len(datafft2)//2][mask0_2], params[0],params[1]), c='sandybrown', label='Fit')
plt.plot(fftfreq2[:len(datafft2)//2][mask0_2], potenza2[1:], label='Segnale originale',c='blue',alpha=0.35)
plt.legend()
plt.yscale('log')
plt.xscale('log')
print('i parametri sono: ',params,' con errori: ',params_err)
plt.show()


params, params_covariance = curve_fit(andamento,xdata=fftfreq3[:len(datafft2)//2][5:], ydata=potenza3[5:])
params_err=np.sqrt(np.diag(params_covariance))
plt.plot(fftfreq3[:len(datafft2)//2][5:], andamento(fftfreq3[:len(datafft2)//2][5:], params[0],params[1]), c='sandybrown', label='Fit')
plt.plot(fftfreq3[:len(datafft2)//2][5:], potenza3[5:], label='Segnale originale',c='green',alpha=0.35)
plt.legend()
plt.yscale('log')
plt.xscale('log')
print('i parametri sono: ',params,' con errori: ',params_err)
plt.show()

# Gli esponenti (restituiti dal secondo parametro) sono: 1.35444518e-02 +- 3.28090305e-02, 0.98456275 +- 1.80123739ee-02,. 1.95668141 +- 0.05578571
# Quindi i diversi rumori sono rispettivamente: Bianco, Rosa e Rosso.