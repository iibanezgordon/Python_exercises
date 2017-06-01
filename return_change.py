# -*- coding: utf-8 -*-
"""
Created on Mon May 29 22:53:12 2017

@author: iibanez

Change Return Program - The user enters a cost and then the amount of money
given. The program will figure out the change and the number of quarters, 
dimes, nickels, pennies needed for the change.
Modification:

The User enters the prize to be payed, and the Amount of money used to be payed.
First the mone is validated ( has to be enough to pay), and then the change is
given
    
The change is given in Euro Coins:
        - 2 euro
        - 1 Euro
        - 50 Cents
        - 20 Cents
        - 10 Cents
        - 5 Cents
        - 2 Cents
        - 1 Cent

"""

def get_price_money():
    print ' Introduce The prize of the goods to be payed\n'
    while True:
        try:
            pre_price = float(raw_input('   '))
            price = round(pre_price,2)
            valid = isinstance(price,float)
            if valid == True:
                break
            else:
                raise
        except:
            print 'The price need to be a number '
    print ' Introduce the money used to pay\n'
    while True:
        try:
            pre_money = float(raw_input('  '))
            money = round(pre_money,2)
            valid = isinstance(money,float)
            if valid == True and money >= price:
                break
            else:
                raise
        except:
            print ' The money needs to be a number, and bigger that the price'
    return(price,money)
            
            
def calc_change(price,money):
    rest = money - price
    if rest == 0:
        print ' There is not return change'
    else:
        temp = int(rest)
        twoeuro = (temp/2)
        rest = rest-(twoeuro*2)
        temp = int(rest)
        euro =temp
        rest = rest - euro
        temp = int(rest*100)
        fiftycents= temp/50
        rest = rest -(fiftycents *50)
        temp = int(rest)
        twentycents =temp/20
        rest = rest -(twentycents*20)
        temp = int(rest)
        tencents = temp/10
        rest = rest -(tencents*10)
        temp = int(rest)
        fivecents= temp/5
        rest = rest -(fivecents*5)
        temp = int(rest)
        twocents = temp/2
        rest = rest - (twocents*2)
        temp = int(rest)
        onecent = temp
        print ' The change is:\n'
        if twoeuro != 0:
            print' {} in coins of 2 Euro\n'.format(twoeuro)
        if euro !=0:
            print' {} in coins of 1 Euro\n'.format(euro)
        if fiftycents != 0:
            print  '{} in coins of fifty cents of Euro\n'.format(fiftycents)
        if twentycents != 0:
            print  '{} in coins of twenty cents of Euro\n'.format(twentycents)
        if tencents != 0:
            print  '{} in coins of ten cents of Euro\n'.format(tencents)
        if fivecents != 0:
            print  '{} in coins of five cents of Euro\n'.format(fivecents)
        if twocents != 0:
            print  '{} in coins of two cents of Euro\n'.format(twocents)
        if onecent != 0:
            print  '{} in coins of one cent of Euro\n'.format(onecent)
            
        
(price,money)=get_price_money()        
calc_change(price,money)       