
"""
BFS
add start position into queue with distance 1
while queue isn't empty 
 - Pop of element 
 - check if they match if so return distance
 - set array of directions    moves = [up, down , right, left ] 
 - Traverse directions for loop
    - if value == 0 and in bounds add not in visited add to queue  with prev dist +1
queue 
[(0,0), 0]
"""

from collections import deque
moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # vist neighbors


def helper_bfs(array, start, end):
    q = deque()
    # store coordinates and distance
    s = [start, 0]
    count = 0
    q.append(s)

    # set as visited
    array[start[0]][start[1]] = 2

    while q:
        curr = q.popleft()
        count = count + 1
        coordinates = curr[0]
        distance = curr[1]
        array[coordinates[0]][coordinates[1]] = 2  # mark as visited

        #  s->g is reached
        if coordinates[0] == end[0] and coordinates[1] == end[1]:
            return [distance, count]

        for x, y in moves:
            row = coordinates[0]
            col = coordinates[1]

            # if in size of 2d array and value is = 0 then add to queue and set as visited
            inbounds = 0 <= row + \
                x < len(array) and 0 <= col + \
                y < len(array) and array[row + x][col + y] == 0
            if inbounds:
                q.append([[row + x, col + y], distance + 1])
                # mark as visited
                array[row + x][col + y] = 2
    return [0, count]
