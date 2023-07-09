#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 20:20:04 2020

@author: Nathan Van Zandt
"""

lc1  =  [ x**2 for x in range(7)]
print(lc1)

words = ['do', 'you', 'comprehend', 'list', 'comprehensions?']
lc2 = [w[len(w)-1::-1] for w in words]
print(lc2)

lc3 = [w[0]+(w[len(w)-1])for w in ['python', 'is', 'very', 'fun!']]
print(lc3)

lc4 = [y%2 for y in range(2, 8)]
print(lc4)

lc5 = [c for c in 'abracadabra' if c != 'a']
print(lc5)


def multiples_of(x, num) :
    """ takes number x and positive int num and returns a 
        list containing num multiplies of x
    """ 
    lc6 = [n*x for n in range(1,num+1)]
    return lc6 
 

def longer_than(n, wordlist) :
    """ takes int n and list wordlist and returns a list of all words 
        from wordlist that are longer than n 
    """
    return [word for word in wordlist if len(word) > n]
  









