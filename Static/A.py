
import queue
import math as m

moves = [(-1,0), (0,-1), (1,0), (0,1)] # vist neighbors 

def helper_a(array, start, end):
    pq = queue.PriorityQueue()

    # pq node structure (estimated priority, array(current coordinate, distance travelled)
    starting_list=[start, 0 , [start]]
    pq.put((0, starting_list))
    count = 0
    array[start[0]][start[1]] = 2

    while not pq.empty():
        # deque and store coordinates and distance into variables
        value = pq.get()
        count = count+1
        coordinates = value[1][0]
        distance = value[1][1]
        path = value[1][2]
        #print('this is inside value ', path)

        parent_list = value[1][2].copy()

        array[coordinates[0]][coordinates[1]] = 2

        # if end goal is reached then return 
        if coordinates[0] == end[0] and coordinates[1] == end[1]:
            return  [distance,count,path]

        for x, y in moves:
            row = coordinates[0]
            col = coordinates[1]

            # if in size of 2d array and value is = 0 then add to queue and set as visited
            inbounds = 0 <= row + x < len(array) and 0 <= col + y < len(array) and array[row + x][col + y] == 0

            if inbounds:
                child_coord = (row + x, col + y)  # coordinate of current position
                child_list = parent_list.copy()
                child_list.append(child_coord)
                est_dist = distance+1 + (m.sqrt((end[0]-child_coord[0])**2 + (end[1]-child_coord[1])**2))  # estimated dist to goal
                child_data = [child_coord, distance + 1, child_list]  # list with current position and total cost thus far

                pq.put((est_dist, child_data))
                array[row + x][col + y] = 2  # mark as visited
    return [0,count,path]
