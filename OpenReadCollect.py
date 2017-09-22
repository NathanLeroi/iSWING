# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 13:49:15 2017

@author: Nathan Leroi
"""

#import urllib.request
#import bs4 as bs
import numpy as np
import urllib.request
import bs4 as bs


def urltxtData():
    
    sauce = urllib.request.urlopen('http://192.168.4.1/buffer').read() #open and read the URL
    soup = bs.BeautifulSoup(sauce,'lxml')      #format the URL to a readable HTML code for parsing
    
    return soup.text.split('\n')     #returns a list of strings after cuting it line by line

def IMUDataArray(lines, i):
    return np.fromstring(lines[i], dtype=float, sep=',')     #return an array of floating numbers, using "," as a divider

#lines = urltxtData()
#
#t = gyroDataArray(0)
#Gx = gyroDataArray(1) 

