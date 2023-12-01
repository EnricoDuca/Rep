import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import integrate


g=9.81
l=0.5

#Definire una funzione pe le equazioni differeziali che descrivono il moto del pendolo semplice

def eq_diff(r,t,l,g):
    theta=r[0]
    omega=r[1]
    f_theta=omega
    f_omega=-g*np.sin(theta)/l
    return np.array([f_theta,f_omega],float)

# Risolvere l'equzione differnziale attraverso scipy.integrate.odeint

theta_0=np.pi/4
omega_0=0

r_0=np.array([theta_0,omega_0])

time=np.linspace(0,10,1000)

yarr  = integrate.odeint(eq_diff, r_0, time, args=(l,g) )

# Grafico Soluzione
fig,ax = plt.subplots(figsize=(9,6))
plt.title('l=0.5 omega = 0 theta = 45')
plt.plot(time,  yarr, label=('theta', 'omega'))
plt.legend(fontsize=14)
plt.show()

#Produrre il grafico di theta in funzione del tempo

theta_t=yarr[:,0]
fig,ax = plt.subplots(figsize=(9,6))
plt.plot(time,theta_t)
plt.xlabel('Time')
plt.ylabel('Theta (l=0.5 omega = 0 theta = 45)')
plt.show()

# Risolvere l'equazione per diverse condizioni iniziali

l2=1

yarr2  = integrate.odeint(eq_diff, r_0, time, args=(l2,g) )

fig,ax = plt.subplots(figsize=(9,6))
plt.title('l=1 omega = 0 theta = 45')
plt.plot(time,  yarr2, label=('theta', 'omega'))
plt.legend(fontsize=14)
plt.show()

r_1=np.array([np.pi/6,0])
yarr3  = integrate.odeint(eq_diff, r_1, time, args=(l,g) )

fig,ax = plt.subplots(figsize=(9,6))
plt.title('l=0.5 omega = 0 theta = 30')
plt.plot(time,  yarr3, label=('theta', 'omega'))
plt.legend(fontsize=14)
plt.show()


# Confrontare in maniera appropriata il grafico di theta vs tempo per le diverse condizioni iniziali

fig,ax=plt.subplots(3,1,sharex=True,figsize=(11,7))

theta_t2=yarr2[:,0]
theta_t3=yarr3[:,0]
ax[0].plot(time,theta_t)
ax[1].plot(time,theta_t2, c='red')
ax[2].plot(time,theta_t3, c='green')
plt.xlabel('Time')
ax[0].set_ylabel('Theta')
ax[1].set_ylabel('Theta1')
ax[2].set_ylabel('Theta2')
plt.show()
