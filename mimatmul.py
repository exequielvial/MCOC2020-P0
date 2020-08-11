# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 20:59:07 2020

@author: Speedy Gonzàlez
"""
import numpy 

def mimatmul(A,B):  #No sé si es necesario decirlo, pero me basé en un código que encontré en stackoverflow
    N = len(A)
    resultado = numpy.zeros((N,N)) #matriz resultante, acá solo tiene ceros
    for m in range(0,N):
        for n in range(0,N):
            for k in range(0,N):
               resultado[m,n] += A[m,k]*B[k,n]
    return resultado