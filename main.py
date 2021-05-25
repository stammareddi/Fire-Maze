
from Dynamic.mainfirearr import create_burning_2d_array
from Static.mainarr import create_2d_array


def main():
    """
    1. have set dim size
    2. have set p values 

    Static Maze  - outline 
    3. for each density get the probability it is visited in BFS
    4. the averages for n matrices based on density p and store it in a nested list

    Result : p = .1  [# of times end is reached in n array, list of averages for n arrays]
    """

    dim = 10  # size of matrix
    p = [.1, .2, .3, .4, .5]  # p values being used

    data = []  # data for plotting

    for density in p:
        # store prob of visited and average nodes visited into array based on the 5 different densities
        data.append(create_2d_array(dim, density))
    # print(create_2d_array(dim,.3))
 
    for d in data:
        print(d)



    # --------Burning Maze---------------------------------------------------------------------------------------------------------
    """
    Burning Mazes 
    Need to create 5 arrays with p = .3 and q being .1,.2,.3,.4,.5 
    for loop trav thru each of q and passing it into helperfunc(array,start,end,p,q[i])
    returns count of success mazes out of n array : [Strategy 1, Strategy 2] for each q 
    """

    # q = [.1, .2, .3, .4, .5]
    #
    # burningdata = []  # stores # of graphs escaped for both strategies for 5 diffrent flame rates
    #
    # for buriningprob in q:
    #     burningdata.append(create_burning_2d_array(dim, .3, buriningprob))
    # # print(create_burning_2d_array(dim,.3,.3))
    #
    # for d in burningdata:
    #     print(d)


if __name__ == "__main__":
    main()


"""
- is problem 4 looking to see how efficient our code is ? yes 
is it possible to have some mazes that have dfs working better? 
- if this is the case would this satisfy the condition of the diagnostic criteria 
all 3 algorithms start from 0,0 to 4,4 yes from Ai 
is it possible for the nodes checked to be the same for BFS and A*?  yes  
should we still return nodes visited for problem 3 even if its not reachable? !!!
problem 4 ? just a writeup



do we have to pass the same firecordinates for both or just one?
avg visted BFS - visted A is this correct formula ? 
"""
