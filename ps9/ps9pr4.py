#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *



class AIPlayer(Player):   

    def __init__(self, checker, tiebreak, lookahead):
        """ put your docstring here
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        
        self.tiebreak = tiebreak 
        self.lookahead = lookahead 
        

    def __repr__(self):
        """ returns a string representing an AIPlayer object. Indicates checker and tiebreak
            strategy.
        """
        s = ''
        c = super().__repr__()
        s += c +' ('+self.tiebreak + ', '+ str(self.lookahead)+')'
        return s
        

    def max_score_column(self, scores):
        """ takes in list of scores for each column 
            and returns the index of max score. If multiple, use tiebreak strategy.
        """
        score_indices = []
        max_score = max(scores)  
        for n in range(len(scores)) : 
            if scores[n] == max_score: 
                score_indices += [n] 
        if len(score_indices) > 1 :
            if self.tiebreak == 'LEFT': 
                return score_indices[0]
            elif self.tiebreak == 'RIGHT' :
                return score_indices[len(score_indices-1)] 
            else : 
                return random.choice(score_indices)
        else:  
            return score_indices[0]
    

    def scores_for(self, board): 
        """must return a list of score - one for each column"""
        scores = [50] * board.width 
        for col in range(board.width) : 
            if board.can_add_to(col) == False :
                scores[col] = -1 
            elif board.is_win_for(self.checker) == True:
                scores[col] = 100 
            elif board.is_win_for(self.opponent_checker()) == True: 
                scores[col] = 0 
            elif self.lookahead == 0 :
                scores[col] = 50
            else : 
                board.add_checker(self.checker, col)
                
                opponent = AIPlayer(self.opponent_checker(),self.tiebreak,self.lookahead-1)
                opp_scores = opponent.scores_for(board)        
                if max(opp_scores) == 0 :
                    scores[col] = 100 
                elif max(opp_scores) == 100 :
                    scores[col] = 0
                elif max(opp_scores) == 50 :
                    scores[col] = 50
                
                board.remove_checker(col)
                
        return scores
    
    
    def next_move(self, b) :
        """takes board  and returns column of best possible move"""
        self.num_moves +=1
        scores = self.scores_for(b)
        return self.max_score_column(scores)
                
                
                
        
       
        
        
        

