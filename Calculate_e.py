# -*- coding: utf-8 -*-
"""
Created on Fri May 26 22:23:02 2017

@author: iibanez
"""
from decimal import *
def factorial(n):
    fac = reduce(lambda x,y: x*y, range(1,n+1))
    return fac





def calculate_e(digits):
    ''' 
    use of the Brothers formula to calculate e
                               (2n+2)
       e=  Sum(n=0 to infinite) ----
                               (2n+1)!
    The max number of digits is 200
    '''
    getcontext().prec = 200
    sum=0
    Decimal(sum)
    for n in range(200):
        num = Decimal(((2*n) + 2))
        denom = factorial((2*n)+1)
        sum += num/denom
    stre = str(sum)
    return stre[0:digits+2]

print calculate_e(200)