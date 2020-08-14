# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 09:52:33 2020

@author: Speedy Gonzàlez
"""
from matplotlib import pyplot
from time import perf_counter
import scipy as sp
import numpy as np
from numpy import float32

def matriz(N, d=float32):
    A = - (np.eye(N, k=-1, dtype = d )) + 2 * \
        (np.eye(N, dtype=d)) + - (np.eye(N, k =+1, dtype=d))
    return A

Ns = [2,5,10,
      12,15,20,30,
      40,45,50,55,
      60,75,100,125,
      160,200,250,350,
      500,600,800,1000,2000,5000,10000]

ciclos = 10

names = ['AinvB.txt','AinvB_npSolve.txt']
files = [open(name,'w') for name in names]

for N in Ns:
    dts = np.zeros((ciclos, len(files)))
    
    for i in range(ciclos):
        
        A = matriz(N)
        B = np.ones(N)
        t1 = perf_counter()
        Ainv = np.linalg.inv(A)
        AinvB = Ainv@B
        t2 = perf_counter()
        dt = t2-t1
        dts[i][0] = dt
        
        A = matriz(N)
        B = np.ones(N)
        t1 = perf_counter()
        AinvB = np.linalg.solve(A, B)
        t2 = perf_counter()
        dt = t2-t1
        dts[i][1]= dt
        

    dts_mean = np.mean(dts, axis = 0)
    print('dts_mean: ', dts_mean)
    
    for j in range(len(files)):
        files[j].write(f'{N} {dts_mean[j]}\n')
        files[j].flush()
    
[file.close() for file in files]

def plotting(names):
    xc = [10,20,50,100,200,500,1000,2000,5000,10000,20000]
    yc = [0.1e-3,1e-3,1e-2,0.1,1,10,60,60*10]
    pyplot.figure()
    
    for name in names:
        data = np.loadtxt(name)
        Ns = data[:,0]
        dts = data[:,1]
        
        pyplot.loglog(Ns, dts.T, '-o',label=name)
        pyplot.ylabel('Tiempo transcurrido')
        pyplot.xlabel('Tamaño de matriz N')
        pyplot.grid(True)
        pyplot.xticks(xc,xc,rotation=45)
        pyplot.yticks(yc,['0.1 ms','1 ms','10 ms','0.1 s','1 s','10 s','1 min','10 min','1 hr'])
    
    pyplot.tight_layout()
    pyplot.legend(loc='upper left')
    pyplot.show()

names = plotting(names)
        
    



