# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 16:00:16 2020

@author: Speedy Gonzàlez
"""
import numpy as np

def crearMatriz(N):
    A = np.identity(N)*2
    i=0
    while i < N:
        if i == 0:
            A[i][1] = -1        
        if i != 0 and i != (N-1):
            A[i][i-1]=-1
            A[i][i+1]=-1                    
        if i == (N-1):
            A[i][N-2] = -1                                
        i+=1    
    return A

    