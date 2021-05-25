from Static.A import helper_a
from collections import deque
from Dynamic.advance_fire_one_step import advance_fire_one_step

#moves = [(-1,0), (0,-1), (1,0), (0,1)] # vist neighbors 

def strategy_a_recalc(array, start, end, prob_burn):
    """
    Get path to take 
    while queue 
        pop of element and mark 2 
        call burn fire maze 
        Is any point on path on fire?   
            call helper arr or snapshot arr 
            remove everything from queue 
            add new list to queue and continue
    """
    copy_arr = array.copy()
    #print("This is the original array:\n", array)
    
    values = helper_a(copy_arr,start,end)  # path to take
    path_to_take = values[2]
    q = deque()
    array[start[0]][start[1]] = 2  # mark as visited 
    #print(path_to_take)


    for cord in path_to_take:
        q.append(cord)
    q.popleft()
    moves = 0
    while q:
        coordinates = q.popleft()  # get coordinate
       
        if array[coordinates[0]][coordinates[1]] == 0:
            array[coordinates[0]][coordinates[1]] = 2  # mark as visited
            moves += 1
            #print("popped coordinate: ", coordinates)
            #print("number of moves made: ", moves)

        if coordinates != start:
            advance_fire_one_step(array,prob_burn)  # get fire
            #print("fire is moving:\n",array)

        if coordinates[0] == end[0] and coordinates[1] == end[1]:  # goal reached
            return True 
        
        if array[coordinates[0]][coordinates[1]] == 5:
            return False

        for c in list(q):
            #print("going through list\n", q)
            #print(c)
            if array[c[0]][c[1]] == 5:
                snap_shot = array.copy()

                # reset visited points
                for row in range(len(snap_shot)):
                    for col in range(len(snap_shot)):
                        if snap_shot[row][col] == 2:
                            snap_shot[row][col] = 0
                #print("this is the snap_shot after visited is reset:\n", snap_shot)

                find_new_path = helper_a(snap_shot,c,end) # get new path from snapshot of that moment
                #print("distance is: ", distance)
                distance = find_new_path[1]
                if distance == 0:
                    return False
                updated_path = find_new_path[2]
                #print("updated path is ", updated_path)
                q.clear()
                for v in updated_path:
                    q.append(v)
                break


    
            
    return False




