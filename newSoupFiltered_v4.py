# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 16:04:50 2017

@author: Nathan Leroi
"""

import matplotlib.pyplot as plt
import numpy as np
import PostProcessing
import OpenReadCollect

arccos = np.arccos
arcsin = np.arcsin
arctan = np.arctan
tan = np.tan
cos = np.cos
sin = np.sin
sqrt = np.sqrt
pi = np.pi
exp = np.exp
log = np.log

fig1=plt.figure()

gy=fig1.add_subplot(3,2,1)
oxz=fig1.add_subplot(3,2,2)
period=fig1.add_subplot(3,2,3)
damp=fig1.add_subplot(3,2,4)
inertia=fig1.add_subplot(3,2,5)

t = []
Gy = []
#Ox = []
ts = []
Os = []
ts = []
T = []
En = []
I = []

m = 11.25
g = 9.81
d = 0.179

m = 5.40
g = 9.81
d = 0.19920

#m = 7.727
#g = 9.81
#d = 0.23855

Oxz = np.zeros(600)

try:
    
    lines = OpenReadCollect.urltxtData()    #calls the function "urltxtData()" from OpenReadCollect.py script and store the list in the variable "lines"
    t = OpenReadCollect.IMUDataArray(lines, 0)    #calls the function "gyroDataArray()" from OpenReadCollect.py script and store the array created into a variable
    Ax = OpenReadCollect.IMUDataArray(lines, 1) 
    Gy = OpenReadCollect.IMUDataArray(lines, 2)    
    
    
#    PostProcessing.cleanUp(Gy, Ax, Oxz)
    
    for n in range(1,600):
        
        Gy[n] = (Gy[n]+Gy[n-1])/2
        Gy[n] = Gy[n]*0.50 + Gy[n-1]*0.50
        
        Ax[n] = Ax[n]*0.10 + Ax[n-1]*0.90
            
    Oxz = arcsin(Ax/9.81)
    
    Oxz = Oxz - np.average(Oxz)
    
    Oxz = Oxz*180/pi
    
    Gy = Gy - np.average(Gy)

    PostProcessing.identifySpikes(Oxz, t, Os, ts)
    
    ts = ts - ts[0]

    PostProcessing.periodDampingInertia(ts, m, g, d, Os, T, En, I)
    
    Ta = np.average(T)
    Tmax = np.max(T)
    Ena = np.average(En)
    Ia = np.average(I)
#    Ia = (m*g*d*(Ta**2)*(1-Ena**2))/(2*pi)**2
    Imax = np.max(I)
    
    print(Ta, Tmax, Ena, Ia, Imax)
    

    gy.clear()
    gy.plot(t,Gy,'g',label='Gy (deg/s)')
    oxz.clear()
    oxz.plot(t,Oxz,'b',label='Oxz (deg)')
    period.clear()
    period.plot(T,'r',label='T (s)')
    damp.clear()
    damp.plot(En,'b',label='En ()')
    inertia.clear()
    inertia.plot(I,'y',label='I (kg.m2)')

    gy.legend()
    oxz.legend()
    period.legend()
    damp.legend()
    inertia.legend()
       
    gy.grid()
    oxz.grid()
    period.grid()
    damp.grid()
    inertia.grid() 
    
    plt.show()
    
except KeyboardInterrupt:
    print('Script Over')