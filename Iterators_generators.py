# -*- coding: utf-8 -*-
"""
Created on Wed May 24 20:31:47 2017

@author: iibanez
"""
def cubos(n):
    '''
    a function is not iterable, therefore that one will always return the
    value of 1*1*1 = 1, becouse only one round of the for will be executed
    '''
    for x in range(1,n+1):
        return x**3



def gencubes(n):
    '''
    this is a generator, and instead each time its executed, it resumes from
    the previous state. That's th first time returns a 1 ( 1**3) the second time
    returns 8 (2*2*2), and so on...
    '''
    for x in range(1, n+1):
        yield x**3

#for x in gencubes(2):
 #   print x
    
def fibonacci(n):
    '''
    generate a fibonacci sequence up to n
    '''
    a=1
    b=1
    for i in range(n):
        yield a
        t = a
        a = b
        b = t + b
        
        
x = fibonacci(10)
print next(x)
print next(x)
x = fibonacci(10)
print next(x)
print next(x)
print next(x)
print next(x)

s = "hola que tal como estamos por aqui"

s = iter(s)
print next(s)


from time import gmtime, strftime
def myGen():
    while True:
        yield strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

print next(myGen())         


def gensquares(N):
    for x in range(1,N+1):
        yield x**2
        
print next(gensquares(3))
print next(gensquares(3))
print next(gensquares(3))

#g = gensquares(10)
#for x in g:
#    print x
#    
#import random
#
#def rand_num(low,high,n):
#    for i in range(1,n+1):
#        yield random.randint(low,high)
#
#for x in rand_num(4,9,23):
#    print x
#    
#s = "hello"
#s_iter = iter(s)
#print next(s_iter)
#print next(s_iter)
#print next(s_iter)
#print next(s_iter)
#print next(s_iter)
#
#
#from math import pi
#
##def get_pi_number(n):
##    for i in range(1,n+1):
#        
#    
