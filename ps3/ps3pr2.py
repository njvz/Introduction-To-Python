#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 12:08:51 2020

@author: Nathan Van Zandt
"""

def cube_evens_lc(values):
    """ takes a list of numbers and returns a list containing 
        the cubes of the even numbers
    """
    lc1 = [v**3 for v in values if v % 2 == 0]
    return lc1


def cube_evens_rec(values):
     """ takes a list of numbers and returns a list containing 
         the cubes of the even numbers 
     """    
     if values == [] :
        return []
     else :
        cube_rest = cube_evens_rec(values[1:])
        if values[0] % 2 == 0 :
            return [values[0]**3] + cube_rest 
        else :
            return cube_rest


def num_occur(c, s):
    """ takes a single char c and string s and returns the  
        number of times c occurs in s 
    """
    return len([l for l in s if l == c]) 


def most_occur(c, words) :
    """ takes a single char c and a list words and returns 
        the string in list with most occurances
    """
    lc1 = [[num_occur(c,s),s] for s in words]
    bestpair = max(lc1)
    return bestpair [1]


def price_string(cents) :
    """ takes a positive integer as given in cents and returns 
        a string in which price is in dollars and cents
    """ 
    d = cents // 100  # compute whole number of dollars
    c = cents - (d * 100)  # compute remaining cents

    ## add code below to build up the price string 
    ## and return it
    if d == 0 and c == 0:
        price = 'nothing' 
    elif d == 0 and c!= 0: 
        price = str(c) + ' cents'
    elif c == 0 and d != 0: 
        price = str(d) + ' dollars'   
    elif d == 1 and c !=1 :
        price = str(d) + ' dollar' + ' and ' + str(c) + ' cents' 
    elif c == 1 and d!= 1 : 
        price = str(d) + ' dollars' + ' and ' + str(c) + ' cent'
    elif c == 1 and d == 1 :
        price = str(d) + ' dollar' + ' and ' + str(c) + ' cent'
    else: 
        price = str(d) + ' dollars' + ' and ' + str(c) + ' cents'
    return price
    
    