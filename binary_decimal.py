# -*- coding: utf-8 -*-
"""
Created on Thu Jun 01 22:46:28 2017

@author: iibanez
Binary to Decimal and Back Converter - Develop a converter to convert 
a decimal number to binary or a binary number to its decimal equivalent.
"""

class number(object):
    def __init__(self, num,dec = True):
        self.num = num
        self.dec = dec
        self.wrong = False
        if self.dec == True:
            self.num = int(num)
        else:
            self.num = str(num)
            for i in num:
                if int(i) >1:
                    print ' Reinstantiate the Class, Binary numbers only have 1 and 0'
                    self.wrong = True
                    break
        if self.wrong == False:
            print self.num
           
    def binary2decimal(self): 
        if self.dec == True:
            print self.num
        else:
            if self.wrong == True:
                print ' Number data corrupted, reinstantiate the class'
            else:
                temp = self.num
                temp =temp[::-1]  
                dec = 0
                pos = 0
                for i in temp:
                    dec += int(i)*(2**pos)
                    pos +=1
                self.num = dec
                print self.num
                
    def decimal2binary(self):
        if self.dec == False:
            print self.num
        else:
            temp = []
            while self.num >0:
                temp.append(self.num%2)
                self.num = self.num/2
            temp = temp[::-1]
            self.num=''
            for i in temp:
                self.num = self.num + str(i) 
            print self.num
            
        
numero = number('101',False)
numero.binary2decimal()
numero2 = number(42)
numero2.decimal2binary()

