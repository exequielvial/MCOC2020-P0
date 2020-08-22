# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 13:57:30 2020

@author: Speedy Gonzàlez
"""
from numpy import *
from scipy.sparse import lil_matrix
import numpy as np

def matriz_laplaciana_llena(N, t=np.float32):

    e = np.eye(N) - np.eye(N,N,1)
    
    return t(e+e.T)

def matriz_laplaciana_dispersa(N, t=np.float32):

    e = eye(N)-eye(N,N,1)
    
    return t(e+e.T)

