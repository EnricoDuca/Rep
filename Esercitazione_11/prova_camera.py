import numpy as np
import ctypes as ct
import sys,os
import pandas as pd
import matplotlib.pyplot as plt

sys.path.append('/Users/enricoduca/Documents/Università/MCF/Rep/Esercitazione_11/read_camera.py')

from read_camera import read

a=read()

width  = 1536
height = 1024
photo=np.zeros((height,width))

x = -1
y = -1
  
pixel_value = -1


for i in range(0,len(a),2):
    x = (i / 2) % width
    y = (i / 2) / width 
    pixel_value = (int.from_bytes(a[i],  byteorder='big', signed=False) + (int.from_bytes(a[i+1],  byteorder='big', signed=False) << 8))
    photo[int(y)][int(x)] = pixel_value

    #print( "%d  %d  -  %d\n", int.from_bytes(a[i],  byteorder='big', signed=False),int.from_bytes(a[i+1],  byteorder='big', signed=False), pixel_value)

plt.imshow(photo,origin='lower',cmap='turbo')

plt.show()