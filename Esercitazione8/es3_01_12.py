import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import integrate

m_molla  = 0.5 # kg
k_molla  = 2  # N/m

omega0 = np.sqrt(k_molla/ m_molla)

def eq_diff(r,t,k,m):
    x=r[0]
    y=r[1]
    dxdt=y
    dydt=-(np.sqrt(k/m)**2)*(x**3)
    return np.array([dxdt,dydt],float)

x_0=0.5
y_0=0.5

r=np.array([x_0,y_0])

time=np.linspace(0,10,1000)

yarr  = integrate.odeint(eq_diff, r, time, args=(k_molla,m_molla) )

# Grafico Soluzione1
fig,ax = plt.subplots(figsize=(9,6))
plt.title('x= {:.1f}m y={:.1f}m/s'.format(r[0],r[1]))
plt.plot(time,  yarr)
plt.ylabel('x e v')
plt.xlabel('t[s]')
plt.legend(fontsize=14)
plt.show()

r_2=np.array([0.2,0.5])

yarr2  = integrate.odeint(eq_diff, r_2, time, args=(k_molla,m_molla) )

# Grafico Soluzione2
fig,ax = plt.subplots(figsize=(9,6))
plt.title('x= {:.1f}m y={:.1f}m/s'.format(r_2[0],r_2[1]))
plt.plot(time,  yarr2)
plt.ylabel('x e v')
plt.xlabel('t[s]')
plt.legend(fontsize=14)
plt.show()

r_3=np.array([1,2])

yarr3  = integrate.odeint(eq_diff, r_3, time, args=(k_molla,m_molla) )

# Grafico Soluzione3
fig,ax = plt.subplots(figsize=(9,6))
plt.title('x= {:.1f}m y={:.1f}m/s'.format(r_3[0],r_3[1]))
plt.plot(time,  yarr3)
plt.ylabel('x e v ') 
plt.xlabel('t[s]')
plt.legend(fontsize=14)
plt.show()

fig,ax=plt.subplots(3,1,sharex=True,figsize=(11,7))

valore1=yarr[:,0]
valore2=yarr2[:,0]
valore3=yarr3[:,0]
ax[0].plot(time,valore1)
ax[1].plot(time,valore2, c='red')
ax[2].plot(time,valore3, c='green')
plt.xlabel('Time[s]')
ax[0].set_ylabel('x1[t] con K = 2')
ax[0].set_title('x= {:.1f}m y={:.1f}m/s'.format(r[0],r[1]))
ax[1].set_ylabel('x2[t] con K = 2')
ax[1].set_title('x= {:.1f}m y={:.1f}m/s'.format(r_2[0],r_2[1]))
ax[2].set_ylabel('x3[t] con K = 2')
ax[2].set_title('x= {:.1f}m y={:.1f}m/s'.format(r_3[0],r_3[1]))
plt.show()

# CAMBIO VALORE DELLA COSTANTE DELLA MOLLA

k_molla2 = 100

fig,ax=plt.subplots(3,1,sharex=True,figsize=(11,7))

yarr_k2  = integrate.odeint(eq_diff, r, time, args=(k_molla2,m_molla) )
yarr2_k2  = integrate.odeint(eq_diff, r_2, time, args=(k_molla2,m_molla) )
yarr3_k2  = integrate.odeint(eq_diff, r_3, time, args=(k_molla2,m_molla) )

valore1_k2=yarr_k2[:,0]
valore2_k2=yarr2_k2[:,0]
valore3_k2=yarr3_k2[:,0]
ax[0].plot(time,valore1_k2)
ax[1].plot(time,valore2_k2, c='red')
ax[2].plot(time,valore3_k2, c='green')
plt.xlabel('Time[s]')
ax[0].set_ylabel('x1[t] con K = 100')
ax[0].set_title('x= {:.1f}m y={:.1f}m/s'.format(r[0],r[1]))
ax[1].set_ylabel('x2[t] con K = 100')
ax[1].set_title('x= {:.1f}m y={:.1f}m/s'.format(r_2[0],r_2[1]))
ax[2].set_ylabel('x3[t] con K = 100')
ax[2].set_title('x= {:.1f}m y={:.1f}m/s'.format(r_3[0],r_3[1]))
plt.show()