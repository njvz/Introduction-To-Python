#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 15:46:56 2020

@author: Nathan Van Zandt
"""

def bitwise_and(b1, b2):
    """ takes two string inputs: b1 and b2 that represent binarry numbers
        and returns the bitwise of the two numbers in string form
    """
    if b1 == '' and b2 == '' :
        return ''
    elif b1 == '' :
        return len(b2) * '0'
    elif b2 == '' :
        return len(b1) * '0'
    else: 
        and_rest = bitwise_and(b1[:-1], b2[:-1])
        if b1[-1] == '1' and b2[-1] == '1' :
            return and_rest + '1' 
        elif b1[-1] == '0' and b2[-1] == '0' :
            return and_rest + '0' 
        elif b1[-1] == '0' and b2[-1] == '1' :
            return and_rest + '0' 
        elif b1[-1] == '1' and b2[-1] == '0' :
            return and_rest + '0' 
        

def add_bitwise(b1, b2):
    """ takes binary numbers, b1 and b2 and returns the sum of b1  
        and b2 in string form
    """
    
    if b1 == ''and b2 == '':
        return '' 
    elif b1 == '':
        return b2
    elif b2 == '':
        return b1 

    else: 
        add_rest = add_bitwise(b1[:-1], b2[:-1])
        if b1[-1] == '0' and b2[-1] == '1' :
            return add_rest + '1'
        elif b1[-1] == '1' and b2[-1] == '0':
            return add_rest + '1' 
        elif b1[-1] == '0' and b2[-1] == '0' :
            return add_rest + '0'
        elif b1[-1] == '1' and b2[-1] == '1':      
            return add_bitwise(add_rest, '1') + '0'