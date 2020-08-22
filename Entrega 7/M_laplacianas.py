# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 13:57:30 2020

@author: Speedy Gonzàlez
"""
from numpy import *
from scipy.sparse import lil_matrix
import numpy as np

def matriz_laplaciana_llena(N, t=np.float32):
#    A = np.identity(N,t) * 2
 #   for i in range (N):
  #      for j in range (N):
   #         if i + 1 == j:
    #            A[i,j] = -1
     #       if i - 1 == j:
      #          A[i,j] = -1 '''
    e = np.eye(N) - np.eye(N,N,1)
    
    return t(e+e.T)

def matriz_laplaciana_dispersa(N, t=np.float32):
#   A = lil_matrix((N,N))
 #   for i in range (N):
  #      for j in range(N):
   #         if i == j:
    #            A[i,j] = 2
     #       if i + 1 == j:
      #          A[i,j] = -1
       #     if i - 1 == j:
        #        A[i,j] = -1'''
    e = eye(N)-eye(N,N,1)
    
    return t(e+e.T)

