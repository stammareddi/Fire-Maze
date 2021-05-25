"""
create_burning_2d_array(array,start,end,p,q[i])
    create random array with density p and one cell selected randomly to have fire 
        check if path exists from start to end 
        check if path exists from start to fire 
    then this array is valid to be used 
    create copies and pass to the diffrent strartgy functions 
        strartegy 1 is almost similiar to A* so we can use that but modify it 
        strategy 2 we have to come up with this...
    returns 2 numbbers which tell us if end goal was reached 
    add to list 
    return list 
"""

from numpy import random
from Static.DFS import helper_dfs

from Dynamic.StrategyOne import strategy_a
from Dynamic.StrategyTwo import strategy_a_recalc
from Dynamic.StrategyThree import strategyThree

def create_burning_2d_array(dim,density,prob_burn):
    strategy1 = 0
    strategy2 = 0
    strategy3 = 0
    x = 0 
    while x<0:
        # create array
        array = random.choice([1, 0], p=[density, 1 - density], size=(dim, dim))
        array[0][0] = 0  # making sure start is always open
        array[dim - 1][dim - 1] = 0  # making sure end is always open

        # random cordinate selected for fire 
        fire_coordinates = random_gen(array)

        # start fire
        array[fire_coordinates[0]][fire_coordinates[1]] = 5

        # check for valid conditions        
        copy_arrEnd = array.copy()
        copy_arrFire = array.copy()
        copy_arrFire[fire_coordinates[0]][fire_coordinates[1]] = 0
        isEndReachable =helper_dfs(copy_arrEnd,(0,0), (dim-1,dim-1)) # returns isvisitedBool , shortest path, # nodes visited
        isFireReachable =helper_dfs(copy_arrFire,(0,0), (fire_coordinates)) # returns isvisitedBool , shortest path, # nodes visited

        if isEndReachable[0] and isFireReachable[0]: # conditons are met 
            #print("orginal array is\n", array)
            strat1arr = array.copy()
            strat2arr = array.copy()
            strat3arr = array.copy()
            #print("Oringal Array is\n", strat2arr)
            strat1 = strategy_a(strat1arr,(0,0),(dim-1,dim-1),prob_burn) #returns boolean 
            strat2 = strategy_a_recalc(strat2arr,(0,0),(dim-1,dim-1),prob_burn) # returns boolean
            strat3 = strategyThree(strat3arr,(0,0),(dim-1,dim-1),prob_burn) # returns boolean
            
           
            #print("printing strat2arr:\n", strat2arr)
            if strat1:
                strategy1 = strategy1+1  
            if strat2:
                strategy2 = strategy2+1  
            if strat3:
                strategy3 = strategy3 +1        
            x = x+1    # increment array  
    return [strategy1,strategy2,strategy3]
      


def random_gen(array):
    while True:
        x = random.choice(len(array)-1)
        y = random.choice(len(array)-1)

        if x!=0 and y !=0 and x!= len(array)-1 and y!=len(array)-1 and array[x][y] == 0:
            return [x,y]
            break


