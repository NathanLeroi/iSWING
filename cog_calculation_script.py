# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 10:03:24 2017

@author: Nathan Leroi
"""

# [cgxs, cgys, cgzs] = Inertia of the Support
# [cgx, cgy, cgz] = Intertia of the Specimen
# [cgXi, cgYi, cgZi] = Inertia of the Support+Specimen with i=1,2,3 (positions)
# [Oxi, Oyi, Ozi] = Offsets of the Specimen's origin with the Support's origin with i=1,2,3 (positions) 
# m = mass Specimen / ms = mass Support / Mt = mass Support+Specimen

"""
   -- 1ST POSITION --

           ^ Ys
           |
           |  ^Y      
           |__|___>Xs
          /   |____>X
      Zs /   /
       L   L  Z

"""

# Input = Ox1, Oz1, cgxs, cgzs, ms

# Output from Spider(CG device) = cgX1, cgZ1, Mt

m = Mt - ms

cgx = ((cgX1*Mt - cgxs*ms)/m) - Ox1

cgz = ((cgZ1*Mt - cgzs*ms)/m) - Oz1


"""
   -- 2ND POSITION --

           ^ Ys
           |
           |     ^X      
           |_____|__>Xs
          /  <___|
      Zs /  Y   /
       L      L  Z

"""

# Input = Ox2, Oz2, cgxs, cgzs, ms, m, Mt

# Output from Spider(CG device) = cgX2, cgZ2

cgy = ((cgXZ*Mt - cgxs*ms)/m) - Ox1

#cgz = ((cgZ2*Mt - cgzs*ms)/m) - Oz2 # Not really needed


"""
Intercalculation to complete the 2 previous results
"""

# Input = [cgx, cgy, cgz]

cgY1 = ((cgy+Oy1)*m + cgys*ms)/Mt

cgY2 = ((cgx+Oy2)*m + cgys*ms)/Mt


"""
   -- 3RD POSITION --

           ^ Ys
           |
           |  ^Z       
           |__|___>Xs
          /   |____>Y
      Zs /   /
       L   L  X

"""

# Input = cgx, cgy, cgz, cgxs, cgys, cgzs, Ox3, Oy3, Oz3, m, ms, Mt 

# Output = cgX3, cgZ3

cgY3 = ((cgz+Oy3)*m + cgys*ms)/Mt

#cgX3 = ((cgy+Ox3)*m + cgxs*ms)/Mt # Only for veryfication maybe

#cgZ3 = ((cgx+Oz3)*m + cgzs*ms)/Mt


""" 

Determination of "d" parameter

I = (m*g*d*(1-E**2)*(T**2))/(4*pi**2)

"""







