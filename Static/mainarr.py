
from numpy import random

from Static.A import helper_a
from Static.DFS import helper_dfs
from Static.BFS import helper_bfs

# creating 2d array


def create_2d_array(dim, density):
    dgf_reached = 0  # counter to check how many out of 10 arrays are reachable
    avg_nodes_visited_bfs = []  # store averages for each array at this density

    x = 0
    is_good_bfs = False
    is_good_dfs = False
    is_good_a = False

    #  create 20 arrays for each density
    while x < 100:

        # create array
        array = random.choice(
            [1, 0], p=[density, 1 - density], size=(dim, dim))
        array[0][0] = 0  # making sure start is always open
        array[dim - 1][dim - 1] = 0  # making sure end is always open

        # print(array)

        copy_dfs = array.copy()
        copy_bfs = array.copy()
        copy_a = array.copy()
       
        # DFS returns count of nodes visited and bool
        value_dfs = helper_dfs(copy_dfs, (0, 0), (dim - 1, dim - 1))
        # BFS returns count of nodes visited
        value_bfs = helper_bfs(copy_bfs, (0, 0), (dim - 1, dim - 1))
        # A returns count of nodes visited
        value_a = helper_a(copy_a, (0, 0), (dim - 1, dim - 1))

        #print("boolean distance count")
        # print(value_dfs[1]) # true distance count
        # print(value_bfs[0]) # distance count
        # print(value_a[0]) # distance count

        # if condition is met for distances travelled
        if value_dfs[1] >= value_bfs[0] >= value_a[0]:
            sum = (value_bfs[1] - value_a[1]) / float(dim * dim)
            avg_nodes_visited_bfs.append(sum)
            # avg_nodes_visited_bfs.append([value_bfs/(20*20)]-[value_a/(20*20)])

            # add prob to see if reached or not
            if value_dfs[0] == True:
                dgf_reached = dgf_reached + 1

            is_good_bfs = True
            is_good_a = True
            is_good_dfs = True

        # check if all conditions are met we can go again with next array
        # if is_good_bfs and is_good_dfs and is_good_a:
        if is_good_a and is_good_bfs and is_good_dfs:
            x += 1

    return [dgf_reached, avg_nodes_visited_bfs]


"""
    variables created 
    for loop for 10 arrays 
        once created call functions on them to get nodes visited, length, goal_reached
        store those values in variables 
    return variables 
"""
