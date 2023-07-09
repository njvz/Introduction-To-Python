#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below.

class Player:
    """data type for a player object with certain attributes"""

    def __init__(self, checker) :
        """constructor for player object"""
        assert(checker == 'X' or checker == 'O')
        self.checker = checker 
        self.num_moves = 0
        

    def __repr__(self):
        """ returns a string representing a player object (Which checker the
            player object is using)
        """
        s = '' 
        if self.checker == 'X':
            s = 'Player X' 
        else :
            s = 'Player O' 
        return s
            
                   
    def opponent_checker(self) :
        """ takes player object self and returns a one charater string representing  
            the checker of the player object's opponent
        """
        if self.checker == 'X' : 
            return 'O'
        else : 
            return 'X'
        
        
    def next_move(self, b): 
        """ takes board object b, player self object and gets a next move for this player  
            that is valid for board b
        """ 
        self.num_moves +=1 
        
        
        while True:
            col = int(input('Enter a column: ')) 
            if col < b.width and b.can_add_to(col) == True:
                return col 
            else : 
                print('Try again!')
            