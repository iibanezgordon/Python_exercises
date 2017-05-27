# -*- coding: utf-8 -*-
"""
Created on Sat May 27 17:35:13 2017

@author: iibanez
"""

def fibonacci(n):
    a=1
    b=1
    for i in range(1,n+1):
        yield a
        a,b = b,a+b
        


while True:
    try:
        info = int(raw_input('Please, Introduce the length of the fibonacci series. '))
        if info > 200:
            raise  
        else:
            break
    except:
            print('Please, introduce an Integer for the length')
            print('The maximum value for the length is 200')
            
fibo= fibonacci(info)
fiboser = []
for n in range(1,info+1):
    temp =next(fibo)
    fiboser.append(temp)
    

for n in fiboser:
    print n
print list(fiboser)