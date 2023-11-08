import numpy as np
import sys,os
import pandas as pd
import matplotlib.pyplot as plt

sys.path.append('reco.py')
sys.path

import reco

file0=pd.read_csv('hit_times_M0.csv')
file1=pd.read_csv('hit_times_M1.csv')
file2=pd.read_csv('hit_times_M2.csv')
file3=pd.read_csv('hit_times_M3.csv')

def crea_array(file):
    arr=[]
    for i in range(0,len(file['hit_time'])):
        arr.append(reco.Hit(file['mod_id'][i],file['det_id'][i],file['hit_time'][i]))
    return arr

a=crea_array(file0)
b=crea_array(file1)
c=crea_array(file2)
d=crea_array(file3)

h=[]
for elem0, elem1, elem2, elem3 in zip(a,b,c,d):
    h.append(elem0)
    h.append(elem1)
    h.append(elem2)
    h.append(elem3)

h_numpy = np.array(h)
h_ordinato = np.sort(h_numpy)

differenze=np.diff(h_ordinato)

mask_differenze = differenze != 0

n, bins, p = plt.hist(np.log10(np.int64(differenze[mask_differenze])), bins=150, color='red', alpha=0.7 )
plt.xlabel('delta t scala logaritmica', fontsize=16)
plt.yscale('log')
plt.show()






