# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 14:15:12 2017

@author: Nathan Leroi
"""

import numpy as np 

cos = np.cos
sin = np.sin
sqrt = np.sqrt
pi = np.pi
log = np.log
arcsin = np.arcsin

def identifySpikes(teta, t, Os, ts):
    
    for n in range(1,598):
        if teta[n]>teta[n-1] and teta[n]>teta[n+1]:
            i = teta[n]
            j = t[n]
    #        k = n
            Os.append(i)      # Os is the angle value of the spikes 
            ts.append(j)      # ts is the time value associated to the spikes
    #        counter.append(k)    # counter allows us to track the address of the spike


def periodDampingInertia(ts, m, g, d, Os, T, En, I):
      
#    ts = ts - ts[0]  #doesn't work for some reason ...
    
    for n in range(1, len(ts)):
        i = ts[n] - ts[n-1]
        T.append(i)            # T is the changing period between 2 spikes
          
        j = log(np.absolute(Os[n-1]/Os[n]))/sqrt((4*pi**2)+(log(np.absolute(Os[n-1]/Os[n])))**2)
        En.append(j)       # En is the estimated damping
        
        k = (m*g*d*(T[n-1]**2)*(1-En[n-1]**2))/(2*pi)**2
        I.append(k)        # I is the inertia estimation based on free oscillation equations (theory of small angles)

#def cleanUp(Gy, Ax, Oxz):
#    
#    for n in range(1,600):
#        
#        Gy[n] = (Gy[n]+Gy[n-1])/2
#        Gy[n] = Gy[n]*0.50 + Gy[n-1]*0.50
#        
#        Ax[n] = Ax[n]*0.10 + Ax[n-1]*0.90
#            
#    Oxz = arcsin(Ax/9.81)
#    Oxz = Oxz - np.average(Oxz)
#    Oxz = Oxz*180/pi
#    
#    Gy = Gy - np.average(Gy)
#    Gy = Gy*180/pi







#def identifySpikes(teta, t, Os, ts, counter):
#    
#    for n in range(1,598):
#        if teta[n]>teta[n-1] and teta[n]>teta[n+1]:
#            i = teta[n]
#            j = t[n]
#            k = n
#            Os.append(i)      # Os is the angle value of the spikes 
#            ts.append(j)      # ts is the time value associated to the spikes
#            counter.append(k)    # counter allows us to track the address of the spike

#def PeriodDampingInertia(ts, m, g, d, Os, counter, Gx, T, En, I, In):
#      
##    ts = ts - ts[0]  #doesn't work for some reason ...
#    
#    for n in range(1, len(ts)):
#        i = ts[n] - ts[n-1]
#        T.append(i)            # T is the changing period between 2 spikes
#          
#        j = log(np.absolute(Os[0]/Os[n]))/sqrt(((2*pi*n)**2)+(log(np.absolute(Os[0]/Os[n])))**2)
#        En.append(j)       # En is the estimated damping
#        
#        k = (m*g*d*(ts[n]**2)*(1-En[n-1]**2))/(2*pi*n)**2
#        I.append(k)        # I is the inertia estimation based on free oscillation equations (theory of small angles)
#        
#        l = (m*g*d*(1+cos(Os[n])))/(((Gx[counter[n]]**2)/2)-8*En[n-1]*((2*pi/T[n-1])**2)*(1-np.sign(Gx[counter[n]])*sin(Os[n]/2)))
#        In.append(l)          
        
        
        
        
        
        
        
        
        
        