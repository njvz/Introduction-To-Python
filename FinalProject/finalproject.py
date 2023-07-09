#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 00:52:37 2020

@author: Nathan Van Zandt
"""
import math

def clean_text(txt) : 
        """ takes a String of text and returns txt without 
            special characters
        """
        s = txt.replace('.','')
        s = s.replace(',','')
        s = s.replace('?','')
        s = s.replace('!','')
        s = s.replace(';','')
        s = s.replace(':','')
        s = s.replace('"','')
    
        s = s.lower().split()
        
        return s

def stem(s):
    """ takes a string as a parameter and returns the stem  
        of s(the root part of the word)
    """
    
    if (s[:3] == 'pre' or s[:3] == 'tri' or s[:3] == 'non' or s[:3] == 'sub') :
        if len(s) > 3:
            s = stem(s[3:]) 
    elif (s[:4] == 'over' or s[:4] == 'fore' or s[:4] == 'ante') :
        if len(s) > 4:
            s = stem(s[4:])
    elif (s[:5] == 'trans' or s[:5] == 'inter' or s[:5] == 'extra' or s[:5] == 'hyper') :
        if len(s) > 5 :
            s = stem(s[5:])
    elif s[-3:] == 'ing' :
        if len(s) == 4 :    
            return s
        elif len(s) > 4 :
            if s[-4] == 'l' and s[-5] == 'l': 
                s = s[:-3]       
            elif s[-4] == s[-5]:
                s = s[:-4] 
        else : 
            s = s[:-3]
    elif s[-2:] == 'er' :
        if len(s) > 3 :
            if s[-3] == s[-4]:
                s = s[:-3] 
        else : 
            s = s[:-2] 
    elif s[-3:] == 'ers' :
        if len(s) > 4:
            if s[-4] == s[-5]:
                s = s[:-4] 
        else : 
           s = s[:-3] 
    elif len(s) == 4 :
        if s[-1] == 'e':
            return s[:-1]
        else :     
            return s
    elif s[-1] == 'y' :
        s = s[:-1] + 'i' 
    elif s[-3:] == 'ies' :
        s = s[:-3] + 'i'
    elif s[-3:] == 'ier' : 
        s = s[:-3] + 'i'  
    elif s[-4:] == 'iers' : 
        s = s[:-4] + 'i'
    elif s[-1] == 's' and len(s) > 3 :
        s = s[:-1]
    
    return s
           

def sample_file_read(filename):
    """ a function that demonstrates how to read a 
        Python dictionary from a file
    """
    f = open(filename, 'r')    # Open for reading.
    d_str = f.read()           # Read in a string that represents a dict.
    f.close()

    d = dict(eval(d_str))      # Convert the string to a dictionary.

    print("Inside the newly-read dictionary, d, we have:")
    print(d)
      

def sample_file_write(filename):
        """ a function that demonstrates how to write a
            Python dictionary to an easily-readable file
        """
        d = {'test': 1, 'foo': 42}   # Create a sample dictionary.
        f = open(filename, 'w')      # Open file for writing.
        f.write(str(d))              # Writes the dictionary to the file.
        f.close()                    # Close the file.
        

class TextModel :
    """Object TextModel"""
    def __init__(self, model_name): 
        """Constructs TextModel object by accepting 
        model_name and initializing three attributes
        """
        self.name  = model_name 
        self.words = {}  #number of times each word appears in the text
        self.word_lengths = {} #number of times each word length appears
        
        self.stems = {} #records the number of times each word stem appears
        self.sentence_lengths = {} #records the number of times each sentence length appears
        self.prefixes = {} #records the number of prefixes
        

    def __repr__(self):
        """return a string representation of the TextModel"""
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n' 
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n' 
        s += '  number of stems: ' + str(len(self.stems)) + '\n'                                     
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += '  number of prefixes: ' + str(len(self.prefixes))
        return s 
    

    def add_string(self, s):
        """ analyzes the string txt and adds its pieces
            to all of the dictionaries in this text model
        """
        words = s.lower()
        words = s.split()
      
        sentence = []
        for word in words:
            if ('.' == word[-1]) or ('?' == word[-1]) or ('!' == word[-1]) :
                sentence += [word]
                if len(sentence) in self.sentence_lengths : 
                    self.sentence_lengths[len(sentence)] += 1
                else : 
                    self.sentence_lengths[len(sentence)] = 1 
                sentence = [] 
            else : 
                sentence += [word]
        
        
        word_list = clean_text(s) 
        
        for w in word_list : 
            self.words[w] = word_list.count(w)
            
        wordlengths = []
        for w in word_list :
            wordlengths += [len(w)]         
        for w in wordlengths :
            self.word_lengths[w] = wordlengths.count(w)
            
        wordstems = []
        for w in word_list :
            wordstems += [stem(w)]         
        for w in wordstems :
            self.stems[w] = wordstems.count(w)
        
        wordprefixes = []
        for w in word_list : 
            if (w[:3] == 'pre' or w[:3] == 'tri' or w[:3] == 'non' or w[:3] == 'sub' or w[:3] == 'mid' or w[:3] == 'mis') :
                if len(w) > 3 :
                    wordprefixes += [w[:3]] 
            elif (w[:4] == 'over' or w[:4] == 'fore' or w[:4] == 'ante' or w[:4] == 'semi') :
                if len(w) >  4 :
                    wordprefixes += [w[:4]]
            elif (w[:5] == 'trans' or w[:5] == 'inter' or w[:5] == 'extra' or w[:5] == 'hyper' or w[:5] == 'super') :
                if len(w) > 5 :
                    wordprefixes += [w[:5]]
        for w in wordprefixes : 
            self.prefixes[w] = wordprefixes.count(w)
        

    def add_file(self, filename) : 
        """adds all of the text in file filenameto the model"""
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        text =  f.read() 
        self.add_string(text)
    
    
    def save_model(self) :
        """saves the TextModel dictionaries by writing them into seperate files"""
        filename1 = self.name + '_' + 'words'
        filename2 = self.name + '_' + 'word_lengths'
        filename3 = self.name + '_' + 'stems'
        filename4 = self.name + '_' + 'sentence_lengths'
        filename5 = self.name + '_' + 'prefixes'
       
        
        d = self.words   
        f = open(filename1, 'w')    
        f.write(str(d))             
        f.close()                    
        
        h = self.word_lengths 
        i = open(filename2, 'w')
        i.write(str(h))
        i.close()  
        
        j = self.stems 
        k = open(filename3, 'w')
        k.write(str(j))
        k.close()
        
        l = self.sentence_lengths 
        m = open(filename4, 'w')
        m.write(str(l))
        m.close()  
        
        n = self.prefixes 
        o = open(filename5, 'w')
        o.write(str(n))
        o.close()  
        

    def read_model(self) : 
        """ reads the stored dictionaries for the called TextModel object from 
            their files and assigns them to the attributes of the called TextModel.
        """
        filename1 = self.name + '_' + 'words'
        filename2 = self.name + '_' + 'word_lengths'
        filename3 = self.name + '_' + 'stems'
        filename4 = self.name + '_' + 'sentence_lengths'
        filename5 = self.name + '_' + 'prefixes' 
        
        f = open(filename1, 'r')   
        d_str = f.read()          
        f.close()

        self.words = dict(eval(d_str))  

        i = open(filename2, 'r')    
        i_str = i.read()         
        i.close()

        self.word_lengths = dict(eval(i_str))  
        
       
        
        j = open(filename3, 'r')    
        j_str = j.read()         
        j.close()

        self.stems = dict(eval(j_str))  
        
        k = open(filename4, 'r')    
        k_str = k.read()         
        k.close()

        self.sentence_lengths = dict(eval(k_str))  
        
        l = open(filename5, 'r')    
        l_str = l.read()         
        l.close()

        self.prefixes = dict(eval(l_str))  
       

    def similarity_scores(self, other):  
        """ takes self and other objects and returns list of log similarity scores measuring 
            the similarity between self and other
        """
        word_score = compare_dictionaries(other.words, self.words)
        word_lengths_score = compare_dictionaries(other.word_lengths, self.word_lengths)
        stems_score = compare_dictionaries(other.stems, self.stems)
        sentence_lengths_score = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
        prefixes_score = compare_dictionaries(other.prefixes, self.prefixes)
    
        scores = []
        scores = scores + [word_score] + [word_lengths_score] + [stems_score] + [sentence_lengths_score] + [prefixes_score]
        return scores
    

    def classify(self, source1, source2):
        """ takes self and source1 and source 2 objects and prints which source is 
            more likely to be the text that has self text in it
        """
        
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        
        weighted_sum1 = 0
        weighted_sum2 = 0
        
        print('scores for '+source1.name+ ' '+str(scores1))
        print('scores for '+source2.name+ ' '+str(scores2))
        
        for x in range(len(scores1)) : 
            weighted_sum1 += scores1[x] / sum(scores1) * scores1[x]
        
        for x in range(len(scores2)) : 
            weighted_sum2 += scores2[x] / sum(scores2) * scores2[x]
            
        if weighted_sum1 > weighted_sum2 :
            print(self.name +' is more likely to have come from '+source1.name)
        else :
            print(self.name +' is more likely to have come from '+source2.name)
        

def compare_dictionaries(d1, d2):
    """takes dictionaries d1 and d2 and returns the log similarity score"""
    score = 0
    total = sum(d1.values()) 
         
    for key in d2 : 
        if key in d1 : 
             score += math.log(d1[key]/total) * d2[key]
        else: 
            if total == 0 :
                score = 0
            else : 
                score += math.log(.5/total) * d2[key]
    return score


def test():
    """ Testing classify function """
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)


def run_tests():
    """ classifying certain textmodels based on greys anatomy and the office
        scripts
    """
    #source textmodels to be compared against 
    source1 = TextModel('The_Office_S3E3')
    source1.add_file('Office_S3E3_Script.txt')

    source2 = TextModel('Greys_Anatomy_S3E1')
    source2.add_file('Greys_S3E1_Script.txt')

    #creating textmodels to classify
    new1 = TextModel('Parks_And_Recreation_S3E2')
    new1.add_file('Parks_S3E2_Script.txt')
    new1.classify(source1, source2)        
    
    new2 = TextModel('House_M.D._S3E1')
    new2.add_file('House_S3E1_Script.txt')
    new2.classify(source1, source2)        
    
    new3 = TextModel('The_Office_S4E4')
    new3.add_file('Office_S4E4_Script.txt')
    new3.classify(source1, source2)        
    
    new4 = TextModel('Greys_Anatomy_S4E1')
    new4.add_file('Greys_S4E1_Script.txt')
    new4.classify(source1, source2)        
    

    
   














     
        