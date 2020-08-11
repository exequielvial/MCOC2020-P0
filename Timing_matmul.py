# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 15:18:39 2020

@author: Speedy Gonzàlez
"""

from scipy import matrix, rand
from time import perf_counter
from matplotlib import pyplot
from mimatmul import mimatmul

colors = ['r','b','g','m','c','y','k','r','b','g']
cont = 0
Ns = [2, 5, 10,
    12, 15, 20,
    30, 40, 45, 50, 55,
    60, 75, 100,
    125, 160, 200,
    250, 350, 500,
    600, 800, 1000,
    2000, 5000, 10000]


    
pyplot.figure()
pyplot.subplot(2,1,1)
while cont < 10:
    x = []
    y = [] 
    mem = []
    pyplot.grid()
    i = 0
    while i<10 :
        N = Ns[i]
        print (N)        
        A = matrix(rand(N,N))
        B = matrix(rand(N,N))
    
        t1 = perf_counter()
        C = mimatmul(A,B)
        t2 = perf_counter()
        
        dt = t2 - t1
        
        memparcial = 3*(N**2)*8
        mem.append(memparcial)
        print(f"Tiempo transcurrido = {dt} s")
        x.append(N)
        y.append(dt)
        
        #pyplot.subplot(2,2,1)
        #pyplot.grid()
       
        pyplot.loglog(x,y,'-o')        
       
        pyplot.plot(x,y,'-o'+colors[cont])
        i +=1
    
    cont += 1

pyplot.grid()

pyplot.ylabel('Tiempo transcurrido')
pyplot.title('Rendimiento A@B')

yc = [0.1e-3,1e-3,1e-2,0.1,1,10,60,60*10,60*60]
pyplot.xticks([10,20,50,100,200,500,1000,2000,5000,10000,20000],[])
pyplot.yticks(yc,['0.1 ms','1 ms','10 ms','0.1 s','1 s','10 s','1 min','10 min','1 hr'])



mc = [10**3,10**4,10**5,10**6,10**7,10**8,10**9,10**10]

pyplot.subplot(2,1,2)
pyplot.loglog(x,mem,'-s')
pyplot.grid(True)
pyplot.xlabel('Tamaño matriz N')
pyplot.ylabel('Uso de memoria')
pyplot.axhline(y=10000000000, xmin=0.001, xmax=0.9999,color='k',ls="--")
pyplot.xticks([10,20,50,100,200,500,1000,2000,5000,10000,20000],[10,20,50,100,200,500,1000,2000,5000,10000,20000],rotation = 45)
pyplot.yticks(mc,['1 KB','10 KB','100 KB','1 MB','10 MB','100 MB','1 GB','10 GB'])

pyplot.show()

