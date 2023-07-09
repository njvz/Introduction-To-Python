#
# ps6pr5.py (Problem Set 6, Problem 5)
#
# TT Securities    
#
# Computer Science 111
#

import math

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    ## Add the new menu options here.
    print('(3) Find the average price')
    print('(4) Find the standard deviation')
    print('(5) Find the max price and its day')
    print('(6) Test a threshold')
    print('(7) Your investment plan')
    print('(8) Quit')


def get_new_prices():
    """gets a new list of prices from the user and returns it"""
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list


def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """
    if len(prices) == 0:
        print('No prices have been entered.')
        return
    
    print('Day Price')
    print('--- -----')
    for i in range(len(prices)):
        print('%3d' % i, end='')
        print('%6.2f' % prices[i])


def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]

## Add your functions for options 3-7 below.

def avg_price(prices) :
    """ returns the average price
        input: prices is a list of 1 or more numbers
    """
    total = 0
    for i in range(len(prices)):
        total += prices[i]
    return total / len(prices)

def std_dev(prices) :
    """ returns the std. dev of the prices
        input: prices is a list of 1 or more numbers
    """
    squarestotal = 0 
    for i in range(len(prices)):
        squarestotal += ((prices[i]-avg_price(prices))**2)
    return math.sqrt(squarestotal/len(prices))


def max_day(prices):
    """returns: the day(index) of the maaximum price
       input: list of 1 or more prices
    """
    x = 0
    index = 0
    for i in range(len(prices)):
        if prices[i] > x:
            x = prices[i]
            index = i
    return index
       

def any_lower(prices,x):
    """ returns: true if there are any prices below x
        input: list of numbers prices and integer x
    """
    result = False
    for i in range(len(prices)):
        if prices[i] < x: 
            result = True
    return result
    

def find_tts(prices):
    """ returns: a list of three numbers showing the best buy date,
        best sell day, and the resulting profit
        input: 2 or more prices
    """
    maxdiff = 0
    buyday = 0
    sellday = 0
    for i in range(len(prices)) :
        for t in range(len(prices)):
            if prices[i] - prices[t] > maxdiff and t < i:
                maxdiff = prices[i] - prices[t]
                buyday = t
                sellday = i
    return [buyday, sellday, maxdiff]
            
            
def tts():
    """the main user-interaction loop"""
    prices = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 8:
            break
        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        ## add code to process the other choices here

        elif choice == 3:
            print('The average price is', avg_price(prices))
        elif choice == 4: 
            print('The standard deviation is', std_dev(prices))
        elif choice == 5:
            print('The max price is', prices[max_day[prices]],'on day',max_day)
        elif choice == 6:            
            x  = int(input('Enter the threshold: '))
            if any_lower(prices,x) == True:
                print('There is at least one price below',x)
            else :
                print('There are no prices below',x)
        elif choice == 7: 
            values = find_tts(prices)
            print('Buy on day',values[0],'at price',prices[values[0]])
            print('Sell on day',values[1],'at price',prices[values[1]])
            print('Total profit:',values[2])
        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')








