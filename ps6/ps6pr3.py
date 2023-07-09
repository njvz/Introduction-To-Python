#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 20:46:31 2020

@author: Nathan Van Zandt
"""

def add_spaces(s) :
    """takes string s and returns s with a space between each pair of adjacent letters"""
    result = ''
    for i in range(len(s)):
        if i == len(s)-1:
            result += s[i]
        else:
            result += s[i] + ' '
    return result


def merge(s1, s2):
    """ takes two strings s1 and s2 and retuans a new string that merges together the 
        characters in s1 and s2
    """ 
    result = '' 
    len_shorter = min(len(s1),len(s2))
    
    for i in range(len_shorter):
        if s1[i] == s2[i] :
            result += s1[i] 
        else: 
            result += s1[i] + s2[i]
        
    if len(s1) > len(s2): 
        result += s1[len_shorter:]
    elif len(s2) > len(s1): 
        result += s2[len_shorter:]
    
    return result


def contains(s, c):
    """ takes string s and single character c and returns true if s  
        contains c, false otherwise 
    """ 
    trueorfalse = False 
    for i in range(len(s)) :
        if s[i] == c:
            trueorfalse = True
    return trueorfalse


def foo(a, b, c):
        a += 4
        c *= b
        print('foo', a, b, c)
        a = bar(c, a)
        print('foo', a, b, c)
        return c

def bar(a, c):
        b = mystery(a)
        print('bar', a, b, c)
        b += mystery(c)
        return b

def mystery(c):
        a = c + 3
        if c > 10:
            a //= 2
        elif c % 3 == 0:
            a += 1
        return a

a = 3
b = 5
c = 2

print(a, b, c)
b = foo(c, a, b)
print(a, b, c)