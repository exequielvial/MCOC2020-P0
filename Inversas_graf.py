# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 09:37:05 2020

@author: Speedy Gonzàlez
"""


from matplotlib import pyplot

def grafico(X,Y,cont, metodo):
    colors = ['b','g','r']
    pyplot.subplot(2,1,1)
    
    pyplot.loglog(X,Y,'-o')        
    pyplot.title('Rendimiento inv ' + metodo )
    if cont ==2:
        metodo = 'scipylinalg overwrite true'
    pyplot.plot(X,Y,'-o'+colors[cont], label =metodo)       
    
        
    pyplot.ylabel('Tiempo transcurrido')
    #pyplot.title('Rendimiento inv ' + metodo )
    yc = [0.1e-3,1e-3,1e-2,0.1,1,10,60,60*10,60*60]
    pyplot.xticks([10,20,50,100,200,500,1000,2000,5000,10000,20000],[])
    pyplot.yticks(yc,['0.1 ms','1 ms','10 ms','0.1 s','1 s','10 s','1 min','10 min','1 hr'])
    

def graficobajo(X,Y):
    mc = [10**3,10**4,10**5,10**6,10**7,10**8,10**9,10**10]
    pyplot.subplot(2,1,2)
    pyplot.grid()
    pyplot.loglog(X,Y,'-ob')        
    pyplot.plot(X,Y,'-o')    
    pyplot.xlabel('Tamaño matriz N')
    pyplot.ylabel('Uso de memoria')
    pyplot.axhline(y=128000, xmin=0.001, xmax=0.9999,color='k',ls="--")
    pyplot.axhline(y=512000, xmin=0.001, xmax=0.9999,color='k',ls="--")
    pyplot.axhline(y=3000000, xmin=0.001, xmax=0.9999,color='k',ls="--")
    pyplot.axhline(y=10000000000, xmin=0.001, xmax=0.9999,color='k',ls="--")
    pyplot.xticks([10,20,50,100,200,500,1000,2000,5000,10000,20000],[10,20,50,100,200,500,1000,2000,5000,10000,20000],rotation = 45)
    pyplot.yticks(mc,['1 KB','10 KB','100 KB','1 MB','10 MB','100 MB','1 GB','10 GB'])
        
        

