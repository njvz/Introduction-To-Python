#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 19:56:37 2020

@author: Nathan Van Zandt
"""
      
        
def first_occur(seq, elem):
    """ takes sequence(list or str) seq and element elem and 
        returns an index of the first occurance of elem in seq
    """ 
    if seq == []:
        return -1 
    elif seq == '':
        return -1    
    else: 
        if seq[0] == elem:
            return 0 
        first_rest = first_occur(seq[1:],elem)
        if first_rest == -1: 
         return - 1
        else: 
         return first_rest + 1   


def last_occur(seq, elem):
    """ takes a sequence(list or str) seq and element elem and 
        returns an index of the last occurance of elem in seq 
    """   
    if seq == []:
        return -1 
    elif seq == '':
        return -1 
    else: 
        last_rest = last_occur(seq[:-1],elem)
        if seq[-1] == elem: 
            return len(seq)-1 
        else:
            return last_rest 


def rem_first(elem, values):
    """removes the first occurrence of elem from the list values"""
    if values == '':
        return ''
    elif values[0] == elem:
        return values[1:]
    else:
        result_rest = rem_first(elem, values[1:])
        return values[0] + result_rest


def jscore(s1,s2) :
    """takes two strings s1 and s2 and returns the number of shared characters"""
    if s1 == '' or s2 == '': 
        return 0 
    else: 
        if s1[0] in s2: 
            jscore_rest = jscore(rem_first(s1[0], s1),(rem_first(s1[0], s2)))
          
            return jscore_rest + 1
        else:
            jscore_rest = jscore(rem_first(s1[0], s1),s2)
            return jscore_rest