import string
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy
from collections import Counter
from scipy import integrate
import sys,os
import argparse

#lettura file
file=pd.read_csv('vel_vs_time.csv')

print(file)
print(file.columns)

t=file['t']
v=file['v']
'''
#grafico della velocita' in funzione del tempo

plt.figure(figsize=(30,5))
plt.errorbar(t,v, yerr=0, fmt='-', color='red')
plt.xlabel('tempo')
plt.ylabel('Velocità')
plt.show()
'''

#calcolo la distanza percorsa in funzione del tempo

scipy_simpson  = scipy.integrate.simpson(v,x=t, dx=0.1)
print('La distanza percorsa é : ', scipy_simpson )


#produrre il grafico della distanza percorsa in funzione del tempo

distanze=[]
for i in range(1, len(v)+1):
    distanze.append(scipy.integrate.simpson(v[:i],t[:i], dx=0.5))
#print(distanze)
'''
plt.figure(figsize=(30,5))
plt.errorbar(t,distanze, yerr=0, fmt='-', color='red')
plt.xlabel('tempo')
plt.ylabel('Distanze')
plt.show()
'''

#usare il modulo argparse per permettere di selezionare il garfico da visualizzare o il file da leggere al momento dell'esecuzione

def parse_arguments():
    
    parser = argparse.ArgumentParser(description='Grafico_e_file.',
                                 usage      ='python3 es1_15_11.py  --opzione')
#    parser.add_argument('-f', '--opzione1',    action='store', type=string,                  help='File da leggere')
    parser.add_argument('-v', '--opzione2',    action='store_true',                          help='Grafico velocità')
    parser.add_argument('-x', '--opzione3',    action='store_true',    help='Grafico distanze')
    return  parser.parse_args()

def main():

    args = parse_arguments()

    # print 
    #print(args)

    if args.opzione2 == True:
        plt.figure(figsize=(30,5))
        plt.errorbar(t,v, yerr=0, fmt='-', color='red')
        plt.xlabel('tempo')
        plt.ylabel('Velocità')
        plt.show()
        print('---------------------------------------------')


    if args.opzione3 == True :
        plt.figure(figsize=(30,5))
        plt.errorbar(t,distanze, yerr=0, fmt='-', color='red')
        plt.xlabel('tempo')
        plt.ylabel('Distanze')
        plt.show()
        print('---------------------------------------------')

if __name__ == "__main__":

    main()
