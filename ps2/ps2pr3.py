#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 13:55:33 2020

@author: Nathan Van Zandt
"""

def move_to_end(s,n): 
    """ takes string s and integer n and returns a string where 
        first n characters of s are moved to the end of the string 
    """
    return s[n:] + s[:n]


def reverse_last(vals, n) :
    """ takes list vals and integer n and returns a new list in  
        which the last n values of vals are reversed and all other  
        values are in original position 
    """
    if n >= len(vals):
        return vals[len(vals)::-1]
    else:
        return vals[:len(vals) - n]  +  vals[len(vals):len(vals) - (n+1):-1]