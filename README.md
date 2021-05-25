# Fire-Maze

The goal of this fire maze was to compare and analyze the efficiency of the 3 different search algorithms. The environment was created with obstacles through the map and a fire being spread. The 3 different algorithms used were Breadth-First Search, Depth First Search, and A* Algorithm with the heuristic being used as the manhattan distance. The obstacle density ranged from .1 to .5. After running the test 20 times. We found the A* algorithm to work the most efficiently. To beat these 3 existing agents the smart agent would run k simulations in all the 8 possible neighbors nodes and see which one has the highest success rate and will take that. The agent will keep on repeating this until it has reached the end goal or has been caught in the fire.This smart agent resulted in a much higher success rate.
