import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import array as arr
import scipy 
from scipy import optimize


file=pd.read_csv('/Users/enricoduca/Documents/Università/MCF/Esercitazione_22_11/Jpsimumu.csv')

#print(file)
#print(file.columns)

#calcolo massa invariante per ogni evento

massa_invariante = np.sqrt((file['E1']+file['E2'])**2-((file['px1']+file['px2'])**2+(file['py1']+file['py2'])**2+(file['pz1']+file['pz2'])**2))

#istogramma della massa invariante calcolata

fig, ax = plt.subplots(figsize=(10,7))

n, bins, p = plt.hist(massa_invariante, bins=200, color='red', alpha=0.7 )
plt.xlabel('Masse invarianti')

#istogramma della massa invariante in un intervallo ristretto attorno al picco più alto

ins = ax.inset_axes([0.6, 0.5, 0.32,0.37])
n, bins, p = ins.hist(massa_invariante, bins=200, range=(2.8, 3.4), color='red', alpha=0.7 )
plt.xlabel('Masse invarianti')
ins.set_title('Picco')
plt.show()

#fit gaussiana singola + polinomiale 

def gaussiana(x,a,m,p1,p0,sigma):
    return a*np.exp(-((x-m)**2)/(2*sigma**2))+p1*x+p0

mask = np.logical_and(massa_invariante<3.4, massa_invariante>2.8)

massa_filtrata= massa_invariante[mask]

print(massa_filtrata)

n2, bins2, p2 = plt.hist(massa_filtrata, bins=200, color='red', alpha=0.7 )
bincenters = (bins2[:-1] + bins2[1:])/2

pstart =  [1.77774830e+02,  3.09296169e+00, -1.68074848e+01,  6.26175324e+01, 2.77727131e-02]
params, params_covariance = optimize.curve_fit(gaussiana, xdata=bincenters, ydata=n2, sigma=np.sqrt(n2), p0=[pstart])

# Grafico risultato fit
plt.plot(bincenters, gaussiana(bincenters, params[0],params[1],params[2],params[3],params[4]), c='blue', label='Fit')
plt.xlabel('Masse invarianti')
plt.ylabel('Eventi / Bin')
plt.legend()
plt.show()

#scarto fra dati e fit

scarti=gaussiana(bincenters, params[0],params[1],params[2],params[3],params[4])-n2

fig, ax = plt.subplots(3,1, figsize=(9,6), gridspec_kw={'height_ratios': [3, 2, 2]}, sharex=True)
fig.subplots_adjust(hspace=0)

ax[0].errorbar(bincenters, n2,  yerr=0, color='royalblue', fmt='o', label='Dati')
ax[0].plot(bincenters, gaussiana(bincenters, params[0],params[1],params[2],params[3],params[4]), color='darkorange' , label='Fit  $\sigma_y$')
ax[0].set_ylabel('Eventi Misurati', fontsize=14)
ax[0].tick_params(axis="y", labelsize=14) 
ax[0].legend(fontsize=14, frameon=False)

ax[1].errorbar(bincenters,  scarti, yerr=np.sqrt(n2), fmt='o', color='royalblue' )
ax[1].axhline(1, color='darkorange')
ax[1].set_ylabel('Scarti',  fontsize =14)
ax[1].tick_params(axis="x",   labelsize=14) 
ax[1].tick_params(axis="y",   labelsize=14) 
ax[1].set_ylim(-60,60)       
ax[1].grid(True, axis='y')

#grafico scarto fra dati e fit diviso per l'errore
ax[2].errorbar(bincenters,  scarti/np.sqrt(n2), yerr=1, fmt='o', color='royalblue' )
ax[2].axhline(1, color='darkorange')
ax[2].set_ylabel('Scarti/errori',  fontsize =14)
ax[2].tick_params(axis="x",   labelsize=14) 
ax[2].tick_params(axis="y",   labelsize=14) 
ax[2].set_ylim(-5,5)       
ax[2].grid(True, axis='y')

plt.show()

# stampare il valore dei parametri del fit e del chi quadro

print('I parametri sono: ', params, ' con rispettivi errori: ', np.sqrt(np.diag(params_covariance)))


# Valore funzine fit ottimizzata in corrispondneza dei tempi dei dati
yfit = gaussiana(bincenters, params[0], params[1], params[2], params[3], params[4])

# chi2
chi2 =  np.sum( (yfit - n2)**2 /n2 ) 

# gradi di libertà
ndof = len(bincenters)-len(params)

print('Chi2 / ndf: {:4.2f} / {:d} = {:2.3f}'.format( chi2, ndof, chi2/ndof ) )

# GAUSSIANA DOPPIA

def gaussiana_2(x,A_1,A_2,sigma_1,sigma_2,m,p_1,p_0):
    return A_1*np.exp(-((x-m)**2)/2*sigma_1**2) + A_2*np.exp(-((x-m)**2)/2*sigma_2**2) + p_1*x + p_0

#Fit gaussiana doppia

n3, bins3, p3 = plt.hist(massa_filtrata, bins=200, color='red', alpha=0.7 )
bincenters2 = (bins3[:-1] + bins3[1:])/2

pstart2 =  [222.48603861, 154.63129155, -48.25114754, -24.65424742,   3.09260852,
 -17.47662313,  66.09232957]

params2, params_covariance2 = optimize.curve_fit(gaussiana_2, xdata=bincenters2, ydata=n3, sigma=np.sqrt(n3), p0=[pstart2])

plt.plot(bincenters2, gaussiana_2(bincenters2, params2[0],params2[1],params2[2],params2[3],params2[4],params2[5],params2[6]), c='blue', label='Fit')
plt.xlabel('Masse invarianti - Gaussiana doppia')
plt.ylabel('Eventi / Bin')
plt.legend()
plt.show()

scarti2=gaussiana_2(bincenters2, params2[0],params2[1],params2[2],params2[3],params2[4],params2[5],params2[6])-n3

fig, ax = plt.subplots(3,1, figsize=(9,6), gridspec_kw={'height_ratios': [3, 2, 2]}, sharex=True)
fig.subplots_adjust(hspace=0)

ax[0].errorbar(bincenters2, n3,  yerr=0, color='royalblue', fmt='o', label='Dati')
ax[0].plot(bincenters2, gaussiana_2(bincenters2, params2[0],params2[1],params2[2],params2[3],params2[4],params2[5],params2[6]), color='darkorange' , label='Fit  $\sigma_y$')
ax[0].set_ylabel('Eventi Misurati', fontsize=14)
ax[0].tick_params(axis="y", labelsize=14) 
ax[0].legend(fontsize=14, frameon=False)

ax[1].errorbar(bincenters2,  scarti2, yerr=np.sqrt(n3), fmt='o', color='royalblue' )
ax[1].axhline(1, color='darkorange')
ax[1].set_ylabel('Scarti',  fontsize =14)
ax[1].tick_params(axis="x",   labelsize=14) 
ax[1].tick_params(axis="y",   labelsize=14) 
ax[1].set_ylim(-50,50)       
ax[1].grid(True, axis='y')

#grafico scarto fra dati e fit diviso per l'errore
ax[2].errorbar(bincenters2,  scarti2/np.sqrt(n3), yerr=1, fmt='o', color='royalblue' )
ax[2].axhline(1, color='darkorange')
ax[2].set_ylabel('Scarti/errori',  fontsize =14)
ax[2].tick_params(axis="x",   labelsize=14) 
ax[2].tick_params(axis="y",   labelsize=14) 
ax[2].set_ylim(-5,5)       
ax[2].grid(True, axis='y')

plt.show()

# stampare il valore dei parametri del fit e del chi quadro

print('I parametri con Gaussiana doppia sono: ',params2, ' con rispettivi errori: ', np.sqrt(np.diag(params_covariance2)))

# Valore funzine fit ottimizzata in corrispondneza dei tempi dei dati
yfit2 = gaussiana_2(bincenters2, params2[0], params2[1], params2[2], params2[3], params2[4], params2[5], params2[6])

# chi2
chi2_2 =  np.sum( (yfit2 - n3)**2 /n3 ) 

# gradi di libertà
ndof_2 = len(bincenters2)-len(params2)

print('Chi2 / ndf: {:4.2f} / {:d} = {:2.3f}'.format( chi2_2, ndof_2, chi2_2/ndof_2 ) )

# ANALISI PICCO AD ENERGIA MAGGIORE

mask3=np.logical_and(massa_invariante<4, massa_invariante>3.4)

massa_filtrata2=massa_invariante[mask3]

n4, bins4, p4 = plt.hist(massa_filtrata2, bins=200, color='red', alpha=0.7 )
bincenters4 = (bins4[:-1] + bins4[1:])/2

pstart4 = [ 2.17244222, 12.95982592, 13.218353,   35.86046351,  3.6843309,  -4.84037915, 22.57207282]

params4, params_covariance4 = optimize.curve_fit(gaussiana_2, xdata=bincenters4, ydata=n4, sigma=np.sqrt(n4), p0=[pstart4])

plt.plot(bincenters4, gaussiana_2(bincenters4, params4[0],params4[1],params4[2],params4[3],params4[4],params4[5],params4[6]), c='blue', label='Fit')
plt.xlabel('Masse invarianti - Gaussiana doppia')
plt.ylabel('Eventi / Bin')
plt.legend()
plt.show()

scarti4=gaussiana_2(bincenters4, params4[0],params4[1],params4[2],params4[3],params4[4],params4[5],params4[6])-n4

fig, ax = plt.subplots(3,1, figsize=(9,6), gridspec_kw={'height_ratios': [3, 2, 2]}, sharex=True)
fig.subplots_adjust(hspace=0)

ax[0].errorbar(bincenters4, n4,  yerr=0, color='royalblue', fmt='o', label='Dati')
ax[0].plot(bincenters4, gaussiana_2(bincenters4, params4[0],params4[1],params4[2],params4[3],params4[4],params4[5],params4[6]), color='darkorange' , label='Fit  $\sigma_y$')
ax[0].set_ylabel('Eventi Misurati', fontsize=14)
ax[0].tick_params(axis="y", labelsize=14) 
ax[0].legend(fontsize=14, frameon=False)

ax[1].errorbar(bincenters4,  scarti4, yerr=np.sqrt(n4), fmt='o', color='royalblue' )
ax[1].axhline(1, color='darkorange')
ax[1].set_ylabel('Scarti',  fontsize =14)
ax[1].tick_params(axis="x",   labelsize=14) 
ax[1].tick_params(axis="y",   labelsize=14) 
ax[1].set_ylim(-12,10)       
ax[1].grid(True, axis='y')

#grafico scarto fra dati e fit diviso per l'errore
ax[2].errorbar(bincenters4,  scarti4/np.sqrt(n4), yerr=1, fmt='o', color='royalblue' )
ax[2].axhline(1, color='darkorange')
ax[2].set_ylabel('Scarti/errori',  fontsize =14)
ax[2].tick_params(axis="x",   labelsize=14) 
ax[2].tick_params(axis="y",   labelsize=14) 
ax[2].set_ylim(-5,5)       
ax[2].grid(True, axis='y')

plt.show()

# stampare il valore dei parametri del fit e del chi quadro

print('I parametri con Gaussiana doppia sono: ',params4, ' con rispettivi errori: ', np.sqrt(np.diag(params_covariance4)))

# Valore funzine fit ottimizzata in corrispondneza dei tempi dei dati
yfit4 = gaussiana_2(bincenters4, params4[0], params4[1], params4[2], params4[3], params4[4], params4[5], params4[6])

# chi2
chi2_4 =  np.sum( (yfit4 - n4)**2 /n4 ) 

# gradi di libertà
ndof_4 = len(bincenters4)-len(params4)

print('Chi2 / ndf: {:4.2f} / {:d} = {:2.3f}'.format( chi2_4, ndof_4, chi2_4/ndof_4 ) )

#La massa risulta essere pari a  (3.6843309 +- 2.67226429e-03)MeV che è compatibile con la massa dello psi(2S) (3686.10 +- 0.06)MeV
