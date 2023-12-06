import scipy 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import fft, constants
from scipy.fft import ifft, rfft, irfft, fft,rfftfreq
from scipy import optimize
from scipy.optimize import curve_fit

# Leggere il file copernicus_PG_selected.csv;

file=pd.read_csv('/Users/enricoduca/Documents/Università/MCF/get-mcf-data/copernicus_PG_selected.csv')

# print(file)
# print(file.columns)

# Produrre un grafico della concentrazione di inquinanti in funzione del tempo;


date_old=file['date_old']
date=file['date']
co=file['mean_co_ug/m3']
nh3=file['mean_nh3_ug/m3']
no2=file['mean_no2_ug/m3']
o3=file['mean_o3_ug/m3']
pm10=file['mean_pm10_ug/m3']
pm2p5=file['mean_pm2p5_ug/m3']
so2=file['mean_so2_ug/m3']

plt.plot(date,co)
plt.plot(date,nh3)
plt.plot(date,no2)
plt.plot(date,o3)
plt.plot(date,pm10)
plt.plot(date,pm2p5)
plt.plot(date,so2)
plt.ylabel('Concentrazioni inquinanti (ug/m3)')
plt.xlabel('Giorni')
plt.show()

# Analizzare i dati per la CO come di seguito

    # Calcolare la trasformata di Fourier della serie temporale

fft_co=rfft(co.values)

dt=1

fftfreq=0.5*rfftfreq(len(co),d=dt)

plt.plot(fftfreq,fft_co)

plt.show()

    # produrre un grafico dello spettro di potenza in funzione della frequenza

potenza=np.abs(fft_co)**2

plt.plot(fftfreq,potenza)

plt.yscale('log')
plt.xscale('log')
plt.ylabel('Potenze (u.a.)')
plt.xlabel('Frequenze (u.a.)')
plt.show()

    #produrre il grafico dello spettro di potenza in funzione del periodo

#Il periodo è un anno 

plt.plot(1/fftfreq[1:],potenza[1:])

plt.yscale('log')
plt.xscale('log')
plt.ylabel('Potenze (u.a.)')
plt.xlabel('Periodo (u.a.)')
plt.show()

# Applicare un filtro ai coefficienti di Fourier selezionando solo le componenti che descrivono l'andamento generale in funzione del tempo (escludendo futtuazioni di breve periodo);

mask_2 = potenza > 10e06
fft_co_filtrato2 = fft_co*mask_2
co_filtrato_2 =irfft(fft_co_filtrato2)

plt.plot(date, co_filtrato_2, label='iFFT - $|c_k|^2>10^7$',c='magenta')
plt.plot(date, co, label='Segnale originale',c='limegreen',alpha=0.5)
plt.legend()
plt.title('data_sample3')
plt.show()
