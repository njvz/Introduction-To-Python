#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 21:18:05 2020

@author: Nathan Van Zandt
"""
from ps4pr1 import *


def mul_bin(b1,b2):
    """ takes two strings b1 and b2 that are binary numbers and 
        returns the numbers multiplied together in string form
    """
    num1 = bin_to_dec(b1)
    num2 = bin_to_dec(b2) 
    product = dec_to_bin(num1*num2)
    return product


def add_bytes(b1,b2):
    """ takes two string b1 and b2 that represent bytes and returns the 
        sum of the bytes 
    """
    num1 = bin_to_dec(b1) 
    num2 = bin_to_dec(b2) 
    sum1 = dec_to_bin(num1+num2)
    lsum1 = len(sum1)
    if lsum1 < 8 : 
        return (8-lsum1) * '0' + sum1
    elif lsum1 > 8 : 
        return sum1[lsum1-8:lsum1]
    else: 
        return sum1
        