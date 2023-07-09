#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 20:27:54 2020

@author: Nathan Van Zandt
"""

def letter_score(letter):
    """ takes in a string letter and returns the score that  
        corresponds with the specific letter 
    """ 
    assert(len(letter)== 1)
    if letter in ['a', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u']:
        return 1
    elif letter in ['d', 'g',]:
        return 2 
    elif letter in ['b', 'c', 'm', 'p']:
        return 3
    elif letter in ['f', 'h', 'v', 'w', 'y']:
        return 4 
    elif letter == 'k': 
        return 5 
    elif letter in ['j', 'x']:
        return 8 
    else :
        return 10 


def scrabble_score(word):
    """takes in a string word and returns a scrabble score of that word""" 
    if word == '' :
        return 0
    else:
        scrabble_score_rest = scrabble_score(word[1:])
        return scrabble_score_rest + letter_score(word[0])
    

def smaller_of(vals1, vals2):
    """ takes two lists vals1 and vals2 and returns a list where each elements  
        is the smaller element between the two 
    """
    if vals1 == [] or vals2 == []:
        return []
    else: 
        smaller_rest = smaller_of(vals1[1:],vals2[1:])
        if vals1[0] < vals2[0]:
            return [vals1[0]] + smaller_rest 
        else : 
            return [vals2[0]] + smaller_rest


def merge(s1, s2):
    """ takes two strings s1 and s2 and returns a new string with characters  
        of both strings merged
    """
    if s1 == '' and s2 == '' :
        return ''
    elif s1 == '' and len(s2) > len(s1) :
        if s1 == '':
            return s2 
    elif s2 == '' and len(s1) > len(s2):
            return s1
    else:
        merge_rest = merge(s1[1:], s2[1:])
        if s1[0] != s2[0]:
            return s1[0] + s2[0] + merge_rest
        else: 
            return s1[0] + merge_rest
    