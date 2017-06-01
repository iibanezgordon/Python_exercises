# -*- coding: utf-8 -*-
"""
Created on Thu Jun 01 22:46:28 2017

@author: iibanez
Binary to Decimal and Back Converter - Develop a converter to convert 
a decimal number to binary or a binary number to its decimal equivalent.
"""

def binary2decimal(number):    
    
    b=str(number) 
    #validation of binary number
    for i in b:
        if int(i) >1:
            print ' Please, Introduce a valid binary number. only 1 and 0'
            valid = False
            break
        else:
            valid = True
     #binary to decimal conversion       
    if valid == True:
        b =b[::-1]  
        dec = 0
        pos = 0
        for i in b:
            dec += int(i)*(2**pos)
            pos +=1
            
        
        print dec

binary2decimal(101)
    
def decimal2binary(number):

    number = int(number)
    temp = []
    while number >0:
        temp.append(number%2)
        number = number/2
    temp = temp[::-1]
    bin=''
    for i in temp:
        bin = bin + str(i) 
    print bin

     
decimal2binary(128)    
     

