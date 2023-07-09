# 
# ps1pr3.py - Problem Set 1, Problem 3
#
# Functions with numeric inputs
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# function 0
def opposite(x):
    """ takes any number (int or float) and returns the opposite of  
        its input
    """
    return -1*x

# put your definitions for the remaining functions below

def root(x):
    """takes num x and returns the square root of x"""
    return x**.5


def gap(num1,num2):
    """returns the “gap” between the two numbers"""
    if num1 < num2:
        return num2 - num1 
    elif num2 < num1: 
        return num1 - num2 
    else: 
        return 0


def larger_gap(a1,a2,b1,b2):
    """ takes 4 numbers a1,a2,b1,b2 and returns the larger gap: either the gap 
        between a1 and a2 or the gap between b1 and b2 
    """
    if gap(a1,a2) > gap(b1,b2) :
        return gap(a1,a2) 
    elif gap(b1,b2) > gap(a1,a2):
        return gap(b1,b2)
    else: 
        return gap(a1,a2) 
    

def median(a, b, c):
    """ takes three numeric inputs a, b, and c, and 
        returns the median of the three inputs 
    """
    if b > a and b < c or b < a and b > c:
        return b 
    elif a > b and a < c or a < b and a > c: 
        return a 
    else:
        return c

# test function with a sample test call for function 0
def test():
    """performs test calls on the functions above"""
    print('opposite(-8) returns', opposite(-8))

    # optional but encouraged: add test calls for your functions below