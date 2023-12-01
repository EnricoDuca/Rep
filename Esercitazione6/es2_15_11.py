import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy
from collections import Counter
from scipy import integrate
import sys,os
import argparse

#schema moto pallina -oscillatore anarmonico-

xx = np.arange(-5,5.05, 0.1)
plt.plot(xx, 0.1*xx**6, color='slategray')
plt.axvline(color='k', linewidth=0.5)
plt.xlabel('x')
plt.ylabel(r'V(x)')
plt.plot(4.5, 0.1*4.5**6, 'o', markersize=12, color='tomato')
plt.show()

#calcolare il periodo in funzione del punto di partenza e utilizzare il modulo argparse per permettere all'utente di scegliere le opzioni sul potenziale da visualizzare.

def parse_arguments():
    
    parser = argparse.ArgumentParser(description='Scelta potenziali.',
                                 usage      ='python3 es2_15_11.py  --opzione')
    parser.add_argument('-6', '--opzione1',    action='store_true',                          help='Opzione1 per V=kx^6')
    parser.add_argument('-4', '--opzione2',    action='store_true',                          help='Opzione2 per V=kx^4')
    parser.add_argument('-2', '--opzione3',    action='store_true',                          help='Opzione3 per V=kx^2')
    return  parser.parse_args()

def main():

    args = parse_arguments()

    # print 
    #print(args)

    m=0.5

    estremi= xx[xx>=0]
    
    def periodi(esponente):
        def V(x):
            return x**esponente
        periodo=[]

        for i in range(2,len(estremi)):
            V_0=V(estremi[i])
            inte=(1/(np.sqrt(V_0-V(estremi)[:i])))
            periodo.append(np.sqrt(8*m)*scipy.integrate.simpson(inte,estremi[:i], dx=0.001))

        plt.errorbar(estremi[3:],periodo[1:], yerr=0, fmt='o', color='red')
        plt.xlabel('x0')
        plt.ylabel('Periodi')
        plt.show()
        print(len(periodo))
        print(len(inte))


    if args.opzione1 == True:
        periodi(6)
        print('---------------------------------------------')
    
    if args.opzione2 == True:
        periodi(4)
        print('---------------------------------------------')

    if args.opzione3 == True:
            periodi(2)
            print('---------------------------------------------')
if __name__ == "__main__":

    main()
