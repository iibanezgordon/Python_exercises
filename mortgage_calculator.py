# -*- coding: utf-8 -*-
"""
Created on Sat May 27 22:35:17 2017

@author: iibanez
**Mortgage Calculator** - 
Calculate the monthly payments of a fixed term mortgage 
over given Nth terms at a given interest rate. Also figure 
out how long it will take the user to pay back the loan.
"""
from types import *

while True:
    try:
        months = int(raw_input("Enter mortgage term (in months): "))
        break
    except:
        print 'Please, Introduce an integer for the number of months'
while True:
    try:
        rate = float(raw_input("Enter interest rate: "))
        break
    except:
        print 'Please, Introduce float number for interest rate'
while True:
    try:
        loan = float(raw_input("Enter loan value: "))
        break
    except:
        print 'Please, Introduce float number for defining the loan'

monthly_rate = rate / 100 / 12
payment = (monthly_rate / (1 - (1 + monthly_rate)**(-months))) * loan

print "Monthly payment for a %.2f euro mortgage, in a %s year mortgage at %.2f%% interest rate, is: $%.2f" % (loan, (months / 12), rate, payment)