#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 20:02:16 2020

@author: Nathan Van Zandt 
"""

# 
# ps1pr5.py - Problem Set 1, Problem 5
#
# Functions on strings and lists, part I
#

def last_first(values):
    """ Takes list values and returns the last 
        value followed by the first value 
    """ 
    last = values[-1]
    first = values[0]
    return [last, first]


def every_other(values) :
    """ takes list values and returns a list containing 
        every other value from values 
    """ 
    return values[0::2]
    

def begins_with(word, prefix): 
    """ takes two strings word and prefix and returns  
        true if word begins with prefix
    """ 
    plength = len(prefix)
    if word[:plength] == prefix :
        return True 
    else:
        return False
    