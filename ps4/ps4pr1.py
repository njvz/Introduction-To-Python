#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 19:10:06 2020

@author: Nathan Van Zandt
"""

def dec_to_bin(n) :
    """ takes a non-negative integer n and returns a string version of 
        binary representation of n
    """
    if n == 1 :
        return '1' 
    elif n == 0 :
        return '0' 
    else :
        dec_rest = dec_to_bin(n // 2)
        if n % 2 == 0 :
            return dec_rest + '0'
        else: 
            return dec_rest + '1'
        
        
def bin_to_dec(b):
    """ takes string b that represents binary number and returns 
        a decimal integer version of b
    """
    if b == '1':
        return 1 
    elif b == '0':
        return 0
    else: 
        bin_rest = bin_to_dec(b[:-1])
        if b[len(b)-1] == '1' :
            return 2 * bin_rest + 1
        else:
             return 2 * bin_rest 
         