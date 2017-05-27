# -*- coding: utf-8 -*-
"""
Created on Sat May 27 18:26:53 2017

@author: iibanez
Prime Factorization - Have the user enter a number and find all Prime Factors 
(if there are any) and display them.

"""
def isprime(n):
    p = 2
    while p < n:
        if n%p == 0:
            return False
        p +=1
    return True


def factorization(n):
    N=n
    primelist = []
    for i in range(2,n+1):
        if isprime(i):
            primelist.append(i)
    length = len(primelist)
    factors = [0]*length
    if length >0:
        for prime in primelist:
            cont = True
            while cont == True:
                if n%prime == 0:
                    cont = True
                    factors[primelist.index(prime)] +=1
                    n=n/prime
                else:
                    cont = False
            
    else:
        print 'the prime factorization is not possible'
    print 'Number {}  has the following prime factorization:'.format(N)
    while True:
        if factors[-1] == 0:
            factors.pop()
        else:
            break
    for i in range(len(factors)):
        print ' {} X {} \n'.format(factors[i], primelist[i] )
    
factorization(8)

                
    
    
    
    
    
    
    
  