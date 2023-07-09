#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 12:42:58 2020

@author: Nathan Van Zandt
"""

def log(b, n) :
    """ takes two integers, b and n and returns the logarithim to  
        the base b of a number n 
    """
    accumulator = 0
    while n > 1 : 
        print("dividing",n,"by",b,"gives",n//b)
        accumulator += 1
        n //= b       
    return accumulator


def add_powers(m, n) :
    """ takes a positive integer m and an arbitray integeer n  
        and returns the sum of the first m powers of n(from n**0 up  
        to and including n**(m-1) power) 
    """
    accumulator = 0
    for i in range(m):
        print(n,"**",i,"=", n ** i)
        accumulator += n**i
    return accumulator


def negate_odds(values):
    """ takes a list of integers values and returns values where all the odd-valued elements are
        replaced with their negated values
    """
    for i in range(len(values)):
        if values[i] % 2 == 1:
            values[i] = -1 * values[i]             
       

 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    