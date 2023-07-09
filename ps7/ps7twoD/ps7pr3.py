#
# ps7pr3.py  (Problem Set 7, Problem 3)
#
# Conway's Game of Life
#
# Computer Science 111  
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# IMPORTANT: this file is for your solutions to Problem 3.
# Your solutions to Problem 2 should go in ps7pr2.py instead.

from ps7pr2 import *


def  alive_neighbors(posnr, posnc,grid):
    """parameter:integer posnr, posnc and 2d list grid
       result: returns  number of 1s around [posnr, posnc] pos.
    
    """
    r = posnr
    c = posnc  
    count = 0

    if grid[r-1][c-1]:
        count+=1
    if grid[r-1][c]:
        count+=1
    if grid[r-1][c+1]:
        count+=1
    if grid[r][c-1]:
        count+=1
    if grid[r][c+1]:
        count+=1
    if grid[r+1][c-1]:
        count+=1
    if grid[r+1][c]:
        count+=1
    if grid[r+1][c+1]:
        count+=1
    
  
    return count

def next_gen(grid) :
    """
    parameter: 2d list grid 
    result: returns new 2-D list representing next generation of cells
    """
    new_grid = copy(grid)
    
    for r in range(1,len(grid)-1):
        for c in range(1,len(grid[0])-1): 
            if alive_neighbors(r,c,grid) < 2:
                new_grid[r][c]=0 
            if alive_neighbors(r,c,grid) > 3:
                new_grid[r][c]=0  
            if grid[r][c] == 0 and alive_neighbors(r,c,grid) == 3:
                new_grid[r][c]= 1  
                
    return new_grid










