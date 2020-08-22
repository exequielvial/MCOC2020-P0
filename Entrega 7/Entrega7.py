# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 19:06:06 2020

@author: Speedy Gonzàlez
"""

import numpy as np
from numpy import *
from scipy.linalg import solve
from time import perf_counter
import matplotlib.pyplot as plt
from M_laplacianas import matriz_laplaciana_llena, matriz_laplaciana_dispersa
from scipy.sparse.linalg import spsolve
from scipy.sparse import csr_matrix

Ns = [5,10,20,50,100, 200, 400, 800, 1000,2000,5000,8000,10000]
plt.figure()
for i in range(5):
    dts = []
    dts1 = []
    for N in Ns:
        t1 = perf_counter()
        
        A = matriz_laplaciana_dispersa(N)
        
        
        t2 = perf_counter()
        X = np.linalg.inv(A)
        
        t3 = perf_counter()
        
        
        dts.append(t2-t1)
        dts1.append(t3-t2)
    
    
    #Gráfico 1
 

    plt.subplot(2,1,1)
    plt.loglog(Ns,dts,'-o',color='0.4')

    yc = [0.1e-3,1e-3,1e-2,0.1,1,10,60,60*10,60*60]
    plt.xticks([5,10,20,50,100, 200, 400, 1000,2000,5000,10000,20000],[])
    plt.yticks(yc,['0.1 ms','1 ms','10 ms','0.1 s','1 s','10 s','1 min','10 min','1 hr'])
    vmin = min(dts)
    plt.ylim(0.00001,dts[-1])
    
    #Gráfico 2
    plt.subplot(2,1,2)    
    plt.loglog(Ns,dts1,'-o', color='0.4')
    plt.yticks(yc,['0.1 ms','1 ms','10 ms','0.1 s','1 s','10 s','1 min','10 min','1 hr'])
    plt.xticks([5,10,20,50,100, 200, 400, 1000,2000,5000,10000,20000],[])

Ns0 = []
Ns2 = []
Ns3 = []
Ns4 = []
Ns02 = []
Ns22 = []
Ns32 = []
Ns42 = []

    
for i in Ns:
    Ns0.append(i*(max(dts)/Ns[-1]))
    Ns02.append(i*(max(dts1)/Ns[-1]))
for i in Ns:
    Ns2.append((i**2)*(max(dts))/(Ns[-1]**2))
    Ns22.append((i**2)*(max(dts1))/(Ns[-1]**2))
for i in Ns:
    Ns3.append((i**3)*(max(dts))/(Ns[-1]**3))
    Ns32.append((i**3)*(max(dts1))/(Ns[-1]**3))
for i in Ns:
    Ns4.append((i**4)*(max(dts))/(Ns[-1]**4))
    Ns42.append((i**4)*(max(dts1))/(Ns[-1]**4))

plt.subplot(2,1,1)
plt.loglog(Ns,Ns0,'--y',label='O(N)')
plt.loglog(Ns,Ns2,'--g',label='O(N**2)')
plt.loglog(Ns,Ns3,'--r',label='O(N**3)')
plt.loglog(Ns,Ns4,'--',label='O(N**4)')
vmax= max(dts)
lv = []
for i in Ns:
    lv.append(vmax)
plt.plot(Ns,lv,'--b', label= 'Constante')
plt.xticks([5,10,20,50,100, 200, 400, 1000,2000,5000,10000,20000],[])
yc = [0.1e-3,1e-3,1e-2,0.1,1,10,60,60*10,60*60]
plt.yticks(yc,['0.1 ms','1 ms','10 ms','0.1 s','1 s','10 s','1 min','10 min','1 hr'])
plt.ylabel('Tiempo de ensamblado')

plt.subplot(2,1,2)
plt.loglog(Ns,Ns02,'--y',label='O(N)')
plt.loglog(Ns,Ns22,'--g',label='O(N**2)')
plt.loglog(Ns,Ns32,'--r',label='O(N**3)')
plt.loglog(Ns,Ns42,'--',label='O(N**4)')
vmax= max(dts1)
lv = []
for i in Ns:
    lv.append(vmax)
plt.plot(Ns,lv,'--b',label='Constante')
plt.ylim(0.00001,dts1[-1])
plt.xticks([5,10,20,50,100, 200, 400, 1000,2000,5000,10000,20000],[5,10,20,50,100, 200, 400, 1000,2000,5000,10000,20000], rotation= 45)
yc = [0.1e-3,1e-3,1e-2,0.1,1,10,60,60*10,60*60]
plt.yticks(yc,['0.1 ms','1 ms','10 ms','0.1 s','1 s','10 s','1 min','10 min','1 hr'])
plt.legend()
plt.ylabel('Tiempo de solución')
plt.xlabel('Tamaño matriz N')

plt.show()
