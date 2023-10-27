import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file=pd.read_csv('4LAC_DR2_sel.csv')

print(file)
print(file.columns)

#stampo un estratto del Data_Frame
print(file.iloc[5:8])

#grafico indice spettrale in funzione del flusso
x=file['Flux1000']
y=file['PL_Index']
plt.scatter(x,y, color='red')
plt.show()

#con asse x logaritmico
plt.plot(x,y, 'o', color='red')
plt.xscale('log')
plt.show()

#grafico in funzione del logaritmo in base 10 della variabile nu_syn

file2=file.loc[( file['nu_syn'] > 0)]

z=file2['nu_syn']
y2=file2['PL_Index']

plt.scatter(z,y2, color='red')
plt.xscale('log')
plt.show()

#grafico distinguendo le sorgenti di classe (CLASS) bll e fsrq con la corrispondente legenda

file_bll=file2.loc[( file2['CLASS'] == 'bll')]
xx=file_bll['nu_syn']
yy=file_bll['PL_Index']
plt.scatter(xx,yy,color='red',alpha=0.9, label='bll')
file_fsrq=file2.loc[( file2['CLASS'] == 'fsrq')]
x3=file_fsrq['nu_syn']
yyy=file_fsrq['PL_Index']
plt.scatter(x3,yyy,color='blue',alpha=0.3, label='fsrq')
plt.xscale('log')
plt.legend(fontsize=14)
plt.show()

#ora anche con l'incertezza
k=file_bll['Unc_PL_Index']
k2=file_fsrq['Unc_PL_Index']
plt.errorbar(xx,yy, yerr=k, fmt='o', color='red', alpha=0.6,label='bll')
plt.errorbar(x3,yyy, yerr=k2, fmt='o', color='blue',alpha=0.6, label='fsrq')
plt.xscale('log')
plt.legend(fontsize=14)
plt.show()

#istogramma sovrapposto dell'indice spettrale per le sorgent di tipo bll e fsrq
n, bins, p = plt.hist(yy, bins=50, range=(1, 5), color='red', alpha=0.4, label='bll')
n, bis, p = plt.hist(yyy, bins=50, range=(1, 5), color='blue', alpha=0.7, label='fsrq')
plt.legend()
plt.show()

#istogramma logaritmico
n, bins, p = plt.hist(np.log10(xx), bins=100, range=(10, 20), color='red', alpha=0.4, label='bll')
n, bis, p = plt.hist(np.log10(x3), bins=100, range=(10, 20), color='blue', alpha=0.7, label='fsrq')
plt.legend()
plt.show()

#grafici con assi condivisi
fig = plt.figure()
gs = fig.add_gridspec(2, 2, hspace=0, wspace=0)
(ax1, ax2), (ax3, ax4) = gs.subplots(sharex='col', sharey='row')
fig.suptitle('Sharing x per column, y per row')
ax1.hist(np.log10(xx), bins=100, range=(10, 20), color='blue', alpha=0.4, label='bll')
ax1.hist(np.log10(x3), bins=100, range=(10, 20), color='gold', alpha=0.7, label='fsrq')
ax2.set_visible(False)
ax3.scatter(np.log10(xx),yy)
ax3.scatter(np.log10(x3),yyy)
ax4.hist(yy,bins=100, range=(1, 3.5), color='blue', alpha=0.4, label='bll', orientation='horizontal')
ax4.hist(yyy,bins=100, range=(1, 3.5), color='blue', alpha=0.4, label='bll',orientation='horizontal')


ax1.set_ylabel('Number of sources')
ax3.set_xlabel('log nu_syn(Hz)')
ax4.set_xlabel('Number of sources')
ax3.set_ylabel('PL Index')

for ax in fig.get_axes():
    ax.label_outer()
plt.show()


