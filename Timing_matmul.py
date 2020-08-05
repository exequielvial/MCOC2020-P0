# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 15:18:39 2020

@author: Speedy Gonzàlez
"""

from scipy import matrix, rand
from time import perf_counter

N = 5

A = matrix(rand(N,N))
B = matrix(rand(N,N))

T1 = perf_counter()
C = A*B
T2 = perf_counter()

tiempoTotal = T2 - T1

print(f'Tiempo transcurrido = {tiempoTotal} segundos')