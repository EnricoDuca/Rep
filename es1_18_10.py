import pandas as pd
import matplotlib.pyplot as plt

file=pd.read_csv('4FGL_J2202.7+4216_weekly_9_11_2023.csv')

print(file)

print(file.columns)

x=file['Julian Date']
y=file['Photon Flux [0.1-100 GeV](photons cm-2 s-1)']
err=file['Photon Flux Error(photons cm-2 s-1)']

plt.plot(x,y, 'o', color='red')
plt.xlabel('Julian Date(days)')
plt.ylabel('Photon Flux [0.1-100 GeV](photons cm-2 s-1)')
#salvo in un file
plt.savefig('Grafico_flusso_fotoni.png')
plt.show()

#grafico con barre d'errore
plt.errorbar(x, y, yerr=err, fmt='o', color='red' )
plt.show()

#grafico con asse y logaritmico

plt.plot(x,y, 'o', color='red')
plt.yscale('log')
plt.savefig('Grafico_flusso_fotoni_log.png')
plt.show()
