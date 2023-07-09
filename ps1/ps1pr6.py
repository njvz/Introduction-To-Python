#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 20:24:37 2020

@author: Nathan Van Zandt
"""

def reverse(s):
    """takes string s and returns the string in reverse"""
    return s[-1::-1]
    

def ends_match(s):
    """ takes string s and returns true if the first character 
        in s matches the last character and false otherwise
    """
    if s[0] == s[-1]:
        return True 
    else: 
        return False 
    

def replace_start(values, new_start_vals):
    """ takes list values and another list new_start_vals 
        and returns a new list where the new_start_vals 
        replace the first n elements in values 
    """ 
    newlistlength = len(new_start_vals) 
    return new_start_vals + values[newlistlength:]


def adjust(s, length): 
    """ takes string s and integer length and returns 
        a string with modified length if necessary
    """
    if length > len(s):
        return s + ((length-len(s)) * s[-1])
    elif length < len(s):
        return s[0:length] 
    else:
        return s
