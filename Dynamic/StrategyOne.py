from collections import deque

import math as m
from numpy import random
from Static.A import helper_a
from Dynamic.advance_fire_one_step import advance_fire_one_step


moves = [(-1,0), (0,-1), (1,0), (0,1)] # vist neighbors 

def strategy_a(array,start,end,prob_burn):

    # get path to take from A* 
    copy_arr = array.copy()
    values = helper_a(copy_arr,start,end)
    path_to_take = values[2]
    q = deque()

    for cord in path_to_take:
        q.append(cord)
    q.popleft()

    array[start[0]][start[1]] = 2  # mark as visited 
    
    while q: 
        coordinates = q.popleft()
        array[coordinates[0]][coordinates[1]] = 2 #mark as visted

        if coordinates != start: # call burn maze after every move
            advance_fire_one_step(array,prob_burn)

        for c in list(q):# checks future path to see if on fire
            if array[c[0]][c[1]] == 5:
                return False 
    return True 






