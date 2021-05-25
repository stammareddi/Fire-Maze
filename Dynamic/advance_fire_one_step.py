from numpy import random
moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # vist neighbors


def advance_fire_one_step(array, prob_burn):
    for row in range(len(array)):  # for each cell
        for col in range(len(array)):  # for each cell
            if array[row][col] == 0 or array[row][col] == 2:  # checks if not burnt cell
                k = 0
                for x, y in moves:  # traverse moves

                    # neighboring cells are caught on fire
                    inbounds = 0 <= row + \
                        x < len(array) and 0 <= col + \
                        y < len(array) and array[row+x][col+y] == 5
                    if inbounds:  # valid burnt neighbor cell
                        k = k+1

                prob = float(1 - (1-prob_burn)**k)
                if random.random() <= prob:
                    array[row][col] = 5
