import pandas as pd 
import numpy as np  
import matplotlib.pyplot as plt
import scipy
from scipy import integrate
import sys
from tqdm import tqdm
from rich.console import Console
from rich.table import Table

# implementi la descrizione della geometria della camera MWPC definendone lo spessore della camera;
# il numero medio di coppie elettrone ione generato dal passaggio di una particella (n_p)
class MWPC:
    def __init__(self,a,b):
        self.spessore = a  
        self.n_p = b
    # implementi la simulazione del passaggio di una particella carica secondo le seguenti specifiche:
    # il numero di coppie elettrone ione primarie deve fluttuare secondo la statistica di Poisson;
    # la posizione delle coppie elettrone ione create deve essere distrubuita con probabilità uniforme lungo lo spessore;
    def passaggio_particella(self):
        numero_coppie_primarie = np.random.poisson(lam=self.n_p)
        posizioni = np.random.uniform(low=-self.spessore/2,high=self.spessore/2,size=numero_coppie_primarie)
        return numero_coppie_primarie,posizioni
    #impementi la simulazione della diffusione degli elettroni:
    # con una componente spazialmente uniforme di passo su;
    # con una componente aggiuntiva di passo sf sempre rivolta verso il filo per simulare l'effetto del campo elettrico;
    # tenendo traccia dello spostamento nella direzione trasversale al piano dei fili e del corrispondnete numero di passi.
    def simulazione_diffusione(self,su,sf,tc,pos,nr):
        x = 0
        y = pos #posizioni elettroni lungo lo spessore(trovato prima)
        elettroni_riassorbiti=np.empty(0)

        passi_tot=np.empty(0)
        
        tempi_deriva=np.empty(0)

        for i in y:
            passi = 0
            count=0
            while abs(i) > 0.01:
                passi=passi+1
                check_assorbimento=np.random.binomial(1,1/nr)
                if (check_assorbimento == 1):
                    elettroni_riassorbiti=np.append(elettroni_riassorbiti,1)
                    count=1
                    break
                else:
                    angolo=np.random.uniform(0,2*np.pi)
                    if (i > 0):
                        x = x  + (su * np.cos(angolo))
                        i = i + (su * np.sin(angolo) - sf)
                    if (i < 0):
                        x = x + (su * np.cos(angolo))
                        i = i + (su * np.sin(angolo) + sf)
            passi_tot=np.append(passi_tot,passi) # passi degli elettroni totale
            if (count == 0):
                tempi_deriva=np.append(tempi_deriva,tc*passi)
        return len(elettroni_riassorbiti), passi_tot, tempi_deriva
        # len(elettroni_riassorbiti, restituisce il numero di elettroni riassorbiti)
        # passi_tot restituisce un array con il numero di passi degli elettroni
        # tempi_deriva restituisce un array con i tempi di deriva degli elettroni

#parametri di prova

n_p = 5
su = 10**(-4)
sf = 5 * 10**(-5)
nr=10**4
tc=10**(-12)

spessore=1

camera=MWPC(spessore,n_p)

# nc,pos=camera.passaggio_particella()
# print('coppie elettrone ione primarie: ',nc,', la posizione delle coppie elettrone ione create è: ',pos)

# num_elettroni_riassorbiti,passi_totali,tempi_deriva_totali=camera.simulazione_diffusione(su,sf,tc,pos,nr)
# print('Il numero di elettroni riassorbiti è: ',num_elettroni_riassorbiti)
# print('I passi totali di ogni elettrone sono: ',passi_totali)
# print('I tempi di deriva di ogni elettrone sono:',tempi_deriva_totali)

class evento:
    def __init__(self,a,b,c,d):
        self.n_gen=a
        self.n_rile=b
        self.td_ril=c
        self.pos0_ril=d

part_generate=[]
part_rilevate=[]
tempi_deriva=[]
posizioni0=[]

numero_test = int(input('Quante particelle si vogliono studiare: '))
for i in tqdm(range(numero_test)):
    nc,pos=camera.passaggio_particella()
    num_elettroni_riassorbiti,passi_totali,tempi_deriva_totali=camera.simulazione_diffusione(su,sf,tc,pos,nr)
    part_generate.append(nc)
    posizioni0.append(pos)
    part_rilevate.append(nc-num_elettroni_riassorbiti)
    tempi_deriva.append(tempi_deriva_totali)

evento_particella=evento(part_generate,part_rilevate,tempi_deriva,posizioni0)

""" per calcolare il minimo tempo di deriva per evento partiamo dalla considerazione che 
un evento è costituito da un generico numero di particelle rilevate che hanno 
a loro volta un determinato tempo di deriva. tempi di deriva è una lista di array
all'interno dei quali ci sono i tempi di deriva. è necessario selezionare il minimo per ognuno 
di questi array"""

tempi_minimi = []
# facciamo la stessa cosa per le medie 
medie_tempi_deriva = []
for x in tempi_deriva:
    if (len(x)>0):
        min = np.min(x)
        media = np.mean(x)
        tempi_minimi.append(min)
        medie_tempi_deriva.append(media)

numero_particella = []
for i in range(numero_test):
    numero_particella.append(i)

tabella =  int(input('1 se si vuole visualizzare la tabella: '))
if (tabella==1):
    console = Console()

    # Dati delle colonne
    colonna1 = [ str(i) for i in numero_particella]
    colonna2 = [ str(i) for i in part_generate]
    colonna3 = [ str(i) for i in part_rilevate]
    #colonna4 = [ str(i) for i in tempi_di_deriva]

 # Creazione della tabella
    table = Table(title="Tabella con 4 colonne")

    # Aggiunta delle colonne
    table.add_column("Num particella", justify="center", style="cyan", no_wrap=True)
    table.add_column("Particelle generate", justify="center", style="magenta", no_wrap=True)
    table.add_column("Particelle rilevate", justify="center", style="yellow", no_wrap=True)
    #table.add_column("Tempi di deriva", justify="center", style="green", no_wrap=True)

    # Aggiunta dei dati alla tabella
    for i in range(len(numero_particella)):
        table.add_row(colonna1[i], colonna2[i], colonna3[i])

    # Stampa della tabella
    console.print(table)

# mostrare la distribuzione delle cariche rilevate 
    
generate =  int(input('1 se si vuole visualizzare la distribuzione delle cariche generate: '))
if (generate==1):
    plt.figure(figsize=[10,8])
    plt.title('Distribuzione delle particelle generate', c='darkred', fontsize = 12)
    n_gen , bins_gen, p_gen = plt.hist(part_generate, bins=25, color='royalblue', label='Data')
    plt.xlabel('Particelle generate')
    plt.ylabel('Eventi/bins')
    plt.legend(loc='upper right')
    plt.show()

rilevate = int(input('1 se si vuole visualizzare la distribuzione delle cariche rilevate: '))
if (rilevate==1):
    plt.figure(figsize=[10,8])
    plt.title('Distribuzione delle particelle rilevate', c='darkred', fontsize = 12)
    n_ril , bins_ril, p_ril = plt.hist(part_rilevate, bins=25, color='royalblue', label='Data')
    plt.xlabel('Particelle rilevate')
    plt.ylabel('Eventi/bins')
    plt.legend(loc='upper right')
    plt.show()

distribuzioni =  int(input('1 per visualizzare il grafico che riporta le distribuzioni: '))
if (distribuzioni==1):
    fig , ax = plt.subplots(2,2, figsize=[10,8])
    fig.suptitle('Distribuzione delle particelle generate e rilevate, tempi minimi e tempi medi di deriva', c='darkred', fontsize = 12)
    ax[0][0].hist(part_generate, bins = 25, label='Generate')
    ax[0][1].hist(part_rilevate, bins = 25, label='Rilevate')
    ax[1][0].hist(tempi_minimi, bins = 25, label='Tempi minimi')
    ax[1][1].hist(medie_tempi_deriva, bins = 25, label='Tempi medi')
    ax[0][0].set_xlabel('Particelle generate')
    ax[0][1].set_xlabel('Particelle rilevate')
    ax[1][0].set_xlabel('Tempi minimi')
    ax[1][1].set_xlabel('Tempi medi di deriva')
    for i in range(0,2):
        for j in range(0,2):
            ax[i][j].legend(loc='upper right')
            ax[i][j].set_ylabel('Eventi/Bins')

    plt.show()