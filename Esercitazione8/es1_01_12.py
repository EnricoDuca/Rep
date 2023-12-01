import numpy as np
import matplotlib.pyplot as plt

V_in= 0.5
RC=1

def funzione_1(V_out,t):
    return (1/(RC))*(V_in-V_out)

a  =  0.
b  = 10.
x0 =  0.


# METODO DI EULERO V_in costante


# Numero di punti utilizzati per la soluzione
N0 = 1000

# separazione fra i punti utilizzati per il calcolo della soluzione h = (b-a)/10 
h = (b-a)/N0

# Array di valori di t equispaziati 
tt = np.arange(a,b,h)

# Array vuoto per contenere i valori della soluzione x(t)
xx = np.empty(0)

# Condizione iniziale 
x = x0

# Ciclo per applicare il metodo di eulero iterativamente 
for t in tt:
    xx = np.append(xx, x)
    x+= h*funzione_1(x,t)
    
# Grafico soluzione 
fig,ax = plt.subplots(figsize=(9,6))
plt.plot(tt,xx)
plt.title('Soluzione con metodo di Eulero - N={:d}'.format(N0), color='slategray')
plt.xlabel('t', fontsize=14)
plt.ylabel('V_out', fontsize=14)
plt.text(tt[0], 0.95*max(xx), r'$\frac{dV_{out}}{dt} = (V_{in} - V_{out})/RC $', color='slategray',fontsize=14)
plt.show()


## RUNGE-KUTTA AL QUARTO ORDINE V_in costante


# Lista con diversi valori di N
NN = [10, 20, 100, 1000]

# Lista con diversi valori di N
NRK4 = [10, 20, 100, 1000]

# Dizionari 
xsolRK4 = {}
tsolRK4 = {}

# Ciclo per diversi N
for n in NRK4: 
    h = (b-a)/n

    tt = np.arange(a,b,h)
    xx = np.empty((0,0))

    x = x0

    # Ciclo per applicare iterativamente il metodo RK4 
    for t in tt:
        xx = np.append(xx, x)
        k1 = h*funzione_1(x,t)
        k2 = h*funzione_1(x+0.5*k1,t+0.5*h)
        k3 = h*funzione_1(x+0.5*k2,t+0.5*h)
        k4 = h*funzione_1(x+k3,t+h)
        x += (k1+k1*2+k3*2+k4)/6 
        
    # Aggiungo soluzioni ai dizionari
    xsolRK4.update({n : xx})
    tsolRK4.update({n : tt})
    
# Grafico soluzioni
fig,ax = plt.subplots(figsize=(9,6))
plt.title('Metodo di Runge-Kutta al Quarto Ordine', color='slategray', fontsize=14)
for n in NN:
    plt.plot(tsolRK4[n],xsolRK4[n], label='{:4d} punti'.format(n))

plt.xlabel('t')
plt.ylabel('V_out')
plt.legend(loc='lower right', fontsize=14)
plt.text(tsolRK4[10][0], 0.95*max(xsolRK4[10]), r'$\frac{dV_{out}}{dt} = (V_{in} - V_{out})/RC$', color='slategray',fontsize=14)
plt.show()

# V_in o +1 o -1 in base alla parità di t

# array tempi 
h = (b-a)/1000
tt = np.arange(a,b,h)

# array V = 1
v = np.ones(len(tt)) 
#maschera per selezionare valori interi dispari (non divisibili per 2) 
odd_mask = tt.astype(int) %2 != 0
print(odd_mask)

# assegno valori per interi dispari
v[odd_mask] = -1

print('v', v)

#METODO EULERO CON V_IN +1 o -1

xx = np.empty(0)

# Condizione iniziale 
x = x0

RC=1

def funzione_2(x,v_in,t):
    return (1/(RC))*(v_in-x)

# Ciclo per applicare il metodo di eulero iterativamente 
for t in range(0,len(tt)):
    xx = np.append(xx, x)
    x += h*funzione_2(x,v[t],t)
# Grafico soluzione 
fig,ax = plt.subplots(figsize=(9,6))
plt.plot(tt,xx)
plt.title('Soluzione con metodo di Eulero - N={:d}'.format(N0), color='slategray')
plt.xlabel('t', fontsize=14)
plt.ylabel('V_out', fontsize=14)
plt.text(tt[0], 0.95*max(xx), r'$\frac{dV_{out}}{dt} = (V_{in} - V_{out})/RC $', color='slategray',fontsize=14)
plt.show()

## RUNGE-KUTTA AL QUARTO ORDINE V_in +1 o -1

# Dizionari 
xsolRK4 = {}
tsolRK4 = {}

# Ciclo per diversi N
h = (b-a)/1000

tt = np.arange(a,b,h)
xx = np.empty((0,0))

x = x0
# Ciclo per applicare iterativamente il metodo RK4 
for t in range(0,len(tt)):
    xx = np.append(xx, x)
    k1 = h*funzione_2(x,v[t],t)
    k2 = h*funzione_2(x+0.5*k1,v[t],t+0.5*h)
    k3 = h*funzione_2(x+0.5*k2,v[t],t+0.5*h)
    k4 = h*funzione_2(x+k3,v[t],t+h)
    x += (k1+k1*2+k3*2+k4)/6 
        
    # Aggiungo soluzioni ai dizionari
    xsolRK4.update({n : xx})
    tsolRK4.update({n : tt})
    
# Grafico soluzioni
fig,ax = plt.subplots(figsize=(9,6))
plt.title('Metodo di Runge-Kutta al Quarto Ordine', color='slategray', fontsize=14)

plt.plot(tt,xx, label='{:4d} punti'.format(n))

plt.xlabel('t')
plt.ylabel('V_out')
plt.legend(loc='lower right', fontsize=14)
plt.show()

#GRAFICO V_IN
fig,ax = plt.subplots(figsize=(9,6))
plt.title('Grafico V_in in funzione del tempo', color='slategray', fontsize=14)
plt.xlabel('t')
plt.ylabel('V_in')
plt.plot(tt,v)
plt.show()

#RISOLVO EQ. DIFF. CON DIVERSI VALORI DI RC

# Lista con diversi valori di RC
RC = [1,0.1,0.01]

# Dizionari per le soluzioni con diversi RC
xsol = {}
tsol = {}

def funzione_3(x,v_in,RC,t):
    return (1/(RC))*(v_in-x)

for rc in RC:
    # Ciclo for sui diversi valori di RC
    h = (b-a)/1000
    
    tt = np.arange(a,b,h)
    xx = np.empty((0,0))

    x = x0
        
    # Ciclo per applicare il metodo di eulero iterativamente 
    for t in range(0,len(tt)):
        xx = np.append(xx, x)
        x += h*funzione_3(x,v[t],rc,t)
        # Aggiungo soluzioni ai dizionari
        xsol.update({rc : xx})
        tsol.update({rc : tt})
    

fig,ax = plt.subplots(figsize=(9,6))
plt.title('Metodo di Eulero', color='slategray', fontsize=14)
for rc in RC:
    plt.plot(tsol[rc],xsol[rc], label='{:.3f} RC'.format(rc))

plt.xlabel('t')
plt.ylabel('V_out')
plt.legend(loc='lower right', fontsize=14)
plt.show()
