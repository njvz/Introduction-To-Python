#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 17:25:43 2020

@author: Nathan Van Zandt
"""
import random

def create_dictionary(filename) :
    """ takes a file and returns a dictionary of keys-value pairs.Each key is a word in the text.
        the corresponfing value is a list of words that follow kew word.
    """
    file = open(filename, 'r') 
    text = file.read()
    file.close()
    words = text.split()
    
    d = {}
    current_word = '$'
    
    for next_word in words:
        if current_word not in d:
            d[current_word] = [next_word] 
        else : 
            d[current_word] += [next_word]
        if '.' in next_word or '!' in next_word or '?' in next_word:
            current_word = '$'
        else :
            current_word = next_word
    return d


def generate_text(word_dict, num_words):
    """ takes a dictionary of word transitions word_dict 
        (generated from word dictionary) and integer num_words. Generates and prints 
        num_words words with a space after each word.
    """
    current_word = '$'
    
    for n in range(num_words) : 
        wordlist = word_dict[current_word]
        next_word = random.choice(wordlist)
        print(next_word, end = ' ')
        if '.' in next_word or '!' in next_word or '?' in next_word:
            current_word = '$'
        else :
            current_word = next_word
    print()
        
        
        

        


    