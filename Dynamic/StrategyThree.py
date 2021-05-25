"""
Need to plan with future fire cells in mind 



3d plan
X:left/right (2d) (3d)
Y: Up/down   (2d) (3d)
Z: step interval  (3d)


One corner of cube to other side of cube passing thru time.
A* or BFS apply equally well to 2d and 3d
z-axis is a count that increases only 


We are looking at future states 

-- simulate how the fire spreads from start to end and 
    try to find what path is good thru that simulated fire


Run Firestep and each call keep count of it until the entire maze is on Fire 


Strat 3(array,start,end)
    Find k steps it take for end to catch on fire 
    # helps us know how many max steps we can take before we die

steps = 0 
while k >= steps: # backtrack out steps to lower steps 
   call fire 

Would finding the k steps it takes for entire maze to catch on fire he

Would finding the total k  steps it takes for entire maze to catch on fire might be helpful?

With this total K steps maybe i run a while loop 


How would fininding the fire spread in the future help here?
    Simulate path from one end to another 
    Find a path between them 





    Basicllay we want to 


    simulate fire spread and look at all possible paths start-->Finish 
        If cell is on Fire call 1 call it 0 if not on fire
        Do it again
    Find path that works for lot of simulations -various way 
    one way. Simualte fire bunch of times average all of simualted Fire mazes and try to find path 
    that hits as little fire as possible 

    Little average fire means most of time it isn't on fire



    simulate fire path from start(one cell on fire) to finish(all cells on fire)  call 1 for fire and 0 for free k = 1
    do it again k = 2 if 



    Bascailly for every current node we run a simulation of k times (we will go with 10) for its neightboirng nodes 
    to see how many times it catches on fire after k moves? Then we get the average prob that that cell will be on fire in k simulations and add it to the list 
    and get the least perctange. Then we add that path to queue and repeat.

    Strat3(arr,start,end):
        add 0,0 to q

        movesMade = 0
        while q is true: 
            curr<-pop of element 

            curr_neightbor_vist_perctange = [] # stores percentage of neightbor cell catching on fire in k simulations
            for curr neighbor cells: # for the neighbor cells 
                countNumOfTimesonFire = 0 # keep tracks num of times its catches on fire in k simulations 
                move = 0 # keeps track of num of simulations 
                while move < k simulations: # while the num of moves is less than k moves 
                    call fire maze and increase move+1 # call fire and incrment move 
                    if neightbor cell on fire increment countNumOfTimesonFire  # check if the neighbor is on fire at k instance          
                divide countNumOfTimesonFire/k simulations *100 and add to curr_neightbor_vist_perctange   
            call fire maze on actual array 
            Add the lowest percantage to queue 




    Find k steps it take for firemaze to reach end goal        



    Strat3(arr,start,end):
        add 0,0 to q

        movesMade = 0
        while q is true: 
            curr<-pop of element 

            curr_neightbor_vist_perctange = [] # stores percentage of neightbor cell catching on fire in k simulations
            for curr neighbor cells: # for the neighbor cells 
                countNumOfTimesonFire = 0 # keep tracks num of times its catches on fire in k simulations 
                move = 0 # keeps track of num of simulations 
                while move < k simulations: # while the num of moves is less than k moves 
                    call fire maze and increase move+1 # call fire and incrment move 
                    Find path 

                    if neightbor cell on fire increment countNumOfTimesonFire  # check if the neighbor is on fire at k instance          
                divide countNumOfTimesonFire/k simulations *100 and add to curr_neightbor_vist_perctange   
            call fire maze on actual array 
            Add the lowest percantage to queue 


"""

"""
simualte fire start to end meaning? --> worst case possible spread 

If path found with Q=1 return True 
else // no path from start to finish that doesnt hit fire in worst case 
    Run simulation with actually q start-->finish ??????????????????? ASK, how many simulations 
        If cell on fire call 1 else 0
        Do it again 
        Average 2 together--> if cell is 0 then both simulations never caught on fire 
                         --> if cell is 1 then both simulations never caught on fire



At each time step find the average each cell is visted after n simulations? 



strat3(array,start,end,burningProb):
    If strat2(array.copy(),start,end,1):
        return True
    Else:
        push start into queue
        
        while q isnt empty:
            value<- pop from queue 

            if value == end:
                return True 
            list = []
            for neighbors for value:
                countofTrues = 0
                while simulations<10 # fire step count 
                    For each step try to
                    data from strategy2(array,value,end,burningProb) [returns True] 
                    simulations++
                    If data is true then countofTrues++
                list.append(countofTrues) [left,up,down,right]
            Push the cordinates with the most trues in queue
    
    Return False
                     

"""
from Static.A import helper_a
from Dynamic.StrategyTwo import strategy_a_recalc
from collections import deque
from Dynamic.advance_fire_one_step import advance_fire_one_step
import math as m

moves = [(-1,0), (0,-1), (1,0), (0,1)] # vist neighbors 
# up/left/down/up

def strategyThree(array,start,end,burningProb):
    #print("hello")
    if strategy_a_recalc(array.copy(),start,end,1):
        return True 
    else:
        q = [] 
        q.append(start)

        while q:

            val = q.pop()
            array[val[0]][val[1]] = 2
            #print("the current value is: ", val)
            #print(array)
            #print(val," ", start, " ", val==start)
            if val != start:
                advance_fire_one_step(array,burningProb) 
            #print("After fire spread\n", array)
            if val == end:
                return True
            highest_success = [0, (0,0), 0]  # success rate / success coordinate / distance to end
            for x,y in moves:  
                inbounds = 0 <= val[0]+ x < len(array) and 0 <= val[1] + y < len(array) and array[ val[0] + x][val[1] + y] == 0 
                success_rate = 0
                if inbounds:
                    simulations = 0 
                    while simulations<10:
                        snapshot_array = array.copy()
                        isTrue = strategy_a_recalc(snapshot_array,(val[0]+x,val[1]+y),end,burningProb)
                        if isTrue:
                            success_rate +=1
                        simulations +=1
                current_coord = (val[0]+x,val[1]+y)
                if current_coord == end:
                    return True
                #print("current coord is: ", current_coord)
                distance_end = m.sqrt((end[0]-current_coord[0])**2 + (end[1]-current_coord[1])**2)
                success_data = [success_rate, (val[0]+x,val[1]+y), distance_end]

                if success_data[0] > highest_success[0]:
                    highest_success[0] = success_data[0]  # only record highest success
                    highest_success[1] = success_data[1]  # records that coordinate
                    highest_success[2] = success_data[2]  # records distance
                elif success_data[0] == highest_success[0] and success_data[2] < highest_success[2]:
                    highest_success[0] = success_data[0]  # only overwrite if distance is smaller
                    highest_success[1] = success_data[1]
                    highest_success[2] = success_data[2]

            #print(highest_success[0])
            if highest_success[0] == 0:
                #print("we have 0 successes")
                return False 
            else:
                #print("new highest success data: ", highest_success)
                q.append(highest_success[1])

    #print("queue has no best next node")           
    return False


