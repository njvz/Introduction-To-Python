# 
# ps8pr1.py - Problem Set 8, Problem 1
#
# String-method puzzles
#

s1 = 'Hickory Dickory Dock!'
s2 = 'The mouse ran up the clock.'

# Example puzzle (puzzle 0):
# Count all occurrences of the letter T (both lower- and upper-case) in s2.
answer0 = s2.lower().count('t')     

# Put your solutions to the remaining string puzzles below.
#Puzzle1
answer1 = s1.replace('ck', 'll')
#Puzzle2 
answer2 = s2.split('e')
#Puzzle3 
answer3 = s1.lower().split('ck')
#Puzzle4
answer4 = s1.upper().replace('D', 'H').replace('HICK','')
#Puzzle5 
answer5 = s2.upper().replace(' ','').replace('N','N ').replace('P', 'P ').split('E')
#Puzzle6


# The code below tests the values of your expressions. DO NOT MODIFY IT!
if __name__ == '__main__':    
    for n in range(0, 6):
        answer_var = 'answer' + str(n)
        if answer_var in dir():
            print(answer_var, '=', eval(answer_var))
            















