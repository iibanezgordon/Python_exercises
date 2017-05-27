# -*- coding: utf-8 -*-
"""
Created on Sat May 27 21:38:18 2017

@author: iibanez

Next Prime Number - Have the program find prime numbers until the user chooses
to stop asking for the next one.

Modification: The user introduces a number. the script calculates the closest 
lower and upper prime number of the given number.
"""

def isprime(n):
    p=2
    while p<n:
        if n%p ==0:
            return False
        p +=1
    return True

def closest_primes(n):
    prime_list =[]
    for i in range(2,n-1):
        if isprime(i):
            prime_list.append(i)
    if len(prime_list) == 0:
        print ' There isnt any prime numbers below the given number'
        lower_prime = 'None'
    else:
        lower_prime = max(prime_list)
    prime_list =[]
    for i in range(n+1, n**2):
        if  isprime(i):
            prime_list.append(i)
    upper_prime = min(prime_list)
    print ' The lower closest prime number is {}\n'.format(lower_prime)
    print ' The upper closest prime number is {}\n'.format(upper_prime)
    

#closest_primes(100)


def find_next_prime():
    print 'welcome to the prime number calculator, the first Prime number is 2\n'
    n=2
    while True:
        while True:
            result = raw_input(' Do you want to know the next prime number? Y/N   ').upper()
            if result == 'Y' or result == 'N':
                break
            else:
                print 'Please, Answer Y (Yes) or N (No)\n'
        if result == 'Y':
           prime = False
           while prime == False:
               prime = isprime(n+1) 
               n +=1
           print ' The next prime number is {}\n'.format(n)
        else:
            print ' thanks for using the Prime calculator, see you soon\n'
            break
        

find_next_prime()
       
                



