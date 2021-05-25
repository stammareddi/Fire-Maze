moves = [(-1,0), (0,-1), (1,0), (0,1)] # vist neighbors 

def helper_dfs(array, start, end):
    stack = [[start, 0]]
    
    while stack:
        value = stack.pop()
        
        coordinates = value[0]
        distance = value[1]

        array[coordinates[0], coordinates[1]] = 2  # mark as visited

        x_val = coordinates[0]
        y_val = coordinates[1]
        if coordinates[0] == end[0] and coordinates[1] == end[1]:
            return [True,distance]

        for x, y in moves:
            inbounds = 0 <= x_val + x < len(array) and 0 <= y_val + y < len(array) and array[x_val + x][y_val + y] == 0
         

            if inbounds:
                stack.append(([x_val+x, y_val+y], distance+1))  # add to stack
                array[coordinates[0], coordinates[1]] = 2  # mark as visited when adding to stack
    return [False,0]
