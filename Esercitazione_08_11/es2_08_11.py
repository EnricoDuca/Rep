import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Legga uno o più file di input;
file0=pd.read_csv('hit_times_M0.csv')
file1=pd.read_csv('hit_times_M1.csv')
file2=pd.read_csv('hit_times_M2.csv')
file3=pd.read_csv('hit_times_M3.csv')

#Produca un istogramma dei tempi per uno dei moduli (file);
n, bins, p = plt.hist(file0['hit_time'], bins=150, color='red', alpha=0.7 )
plt.xlabel('Hit time ', fontsize=16)
plt.show()

#Produca un istogramma delle differenze di tempi fra Hit consecutivi per uno dei moduli;
h=np.diff(file0['hit_time'])
mask = h !=0
n_diff, bins_diff, p_diff = plt.hist(np.log10(h[mask]), bins=200, color='red', alpha=0.7 )
plt.xlabel(' delta Hit time logaritmico ', fontsize=16)
plt.show()