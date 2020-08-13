# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 09:20:08 2020

@author: Speedy Gonzàlez
"""
import scipy
from time import perf_counter
import numpy as np
from Inversas_graf import grafico, graficobajo
from matplotlib import pyplot
from Matrices import crearMatriz



Ns = [2, 3, 4, 5, 10,
    12, 15, 20,
    30, 40, 45, 50, 55,
    60, 75, 100,
    125, 160, 200,
    250, 350, 500,
    600, 800, 1000,
    2000, 5000]



def numpylinalg():
    Cnp = []
    tiempo0 = []
    for N in Ns:    #N va tomando los distintos valores de la lista Ns

        A = crearMatriz(N)
        #np.half(A)
        #np.single(A)
        #np.double(A)
        np.longdouble(A)
        print(A)
        t1 = perf_counter()
        C = np.linalg.inv(A)
        #np.half(C)
        #np.single(C)
        #np.double(C)
        np.longdouble(C)
        Cnp.append(C)
        t2 = perf_counter()
        dt = t2 - t1
        #np.half(dt)
        #np.single(dt)
        #np.double(dt)
        np.longdouble(dt)
        tiempo0.append(dt)
        
    return Cnp,tiempo0
    
def scipylinalg():
    Csp =[]
    tiempo1 = []
    for N in Ns:    #N va tomando los distintos valores de la lista Ns
        A = crearMatriz(N)
        #np.half(A)
        #np.single(A)
        #np.double(A)
        np.longdouble(A)
        t1 = perf_counter()
        C = scipy.linalg.inv(A)
        #np.half(C)
        #np.single(C)
        #np.double(C)
        np.longdouble(C)
        Csp.append(C)
        t2 = perf_counter()
        dt = t2 - t1
        #np.half(dt)
        #np.single(dt)
        #np.double(dt)
        np.longdouble(dt)
        tiempo1.append(dt)
        
    return Csp,tiempo1

def scipylinalgoverwrite():
    Cspov = []
    tiempo2 = []
    mem = []
    for N in Ns:    #N va tomando los distintos valores de la lista Ns
        A = crearMatriz(N)
        #np.half(A)
        #np.single(A)
        #np.double(A)
        np.longdouble(A)
        t1 = perf_counter()
        C = scipy.linalg.inv(A,overwrite_a=True, check_finite=True)
        #np.half(C)
        #np.single(C)
        #np.double(C)
        np.longdouble(C)
        Cspov.append(C)
        t2 = perf_counter()
        dt = t2 - t1
        #np.half(dt)
        #np.single(dt)
        #np.double(dt)
        np.longdouble(dt)
        tiempo2.append(dt)
        
        #memparcial = 2*(N**2)*16 # Half
  #      memparcial = 2*(N**2)*32 # Single
        #memparcial = 2*(N**2)*64 # Double
        
        memparcial = 2*(N**2)*128 # longdouble
        mem.append(memparcial)
        
    return Cspov, tiempo2,mem

cont= 0
rendnp = numpylinalg()    
grafico(Ns,rendnp[1],cont,'numpylinalg')
cont +=1
rendsp = scipylinalg()
grafico(Ns,rendsp[1],cont,'scipylinalg')
cont =2
pyplot.grid()
rendspov = scipylinalgoverwrite()

#grafico(Ns,rendspov[1],cont,'dato tipo half')
#grafico(Ns,rendspov[1],cont,'dato tipo single')
#grafico(Ns,rendspov[1],cont,'dato tipo double')
grafico(Ns,rendspov[1],cont,'dato tipo longdouble')

pyplot.legend()
graficobajo(Ns,rendspov[2])



 

#pyplot.grid()   
pyplot.show()
