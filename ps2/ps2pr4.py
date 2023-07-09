#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 19:28:04 2020

@author: Nathan Van Zandt
"""

def repeat(s, n):
    """ takes string s and integer n and returns a string in  
        which n copies of s have been concatenated together 
    """ 
    if n == 0 :
        return ''
    elif n == 1:
        return s
    else:
        repeat_rest = repeat(s, n-1)
        return s + repeat_rest
        
    
def contains(s, c):
    """ takes string s and char c and returns true if s  
        contains c or false if s doesnt contain c 
    """
    if s == '' :
        return False 
    elif s[0] == c :
        return True
    else: 
        contains_rest = contains(s[1:], c)
        if contains_rest == True:
                return contains_rest
        else:
            return False


def add(vals1,vals2):
    """ takes two lists, vals1 and vals2 and returns a new list in 
        which each element is the sum of original lists 
    """
    if vals1 == [] or vals2 == []:
        return []
    elif len(vals1) != len(vals2):
        return []
    else: 
        add_rest = add(vals1[1:],vals2[1:])
        return [vals1[0] + vals2[0]] + add_rest
         
       
def contains1(s, c):
    """ takes string s and char c and returns true if s contains c or 
        false if it does'nt 
    """ 
    if s == '' :
        return False 
    if s[0] == c:
        return True 
    else: 
        contains_rest = contains(s[1:], c)
        if contains_rest == True :
            return contains_rest 
        else: 
            return False
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    