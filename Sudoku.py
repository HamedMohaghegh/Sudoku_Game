# Sudoku Game Initialization

# Importing the random module for shuffling numbers
import random

# Initialize empty lists to store Sudoku board and column-wise numbers
my_list = [[], [], [], [], [], [], [], [], []]
my_list_column = [[], [], [], [], [], [], [], [], []]

# Initialize the Sudoku game board with a 9x9 grid
my_game = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


def new_game(my_list, my_list_column, my_game):
    # Iterate through each row in the Sudoku board
    for i in range(9):
        while True:
            # Reset variables for each iteration
            my_list_true = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            limit = 0

            # Iterate through each column in the current row
            for j in range(9):
                check = True

                # Choose a random number not present in the current column
                while check:
                    x = random.choice(my_list_true)
                    if x not in my_list_column[j]:
                        my_list_true.remove(x)
                        my_list_column[j].append(x)
                        check = False
                        my_list[i].append(x)
                    else:
                        check = True
                        limit += 1

                    # If the limit is reached, restart the current row
                    if limit == 10:
                        break

                # If the limit is reached, restart the current row
                if limit == 10:
                    my_list[i].clear()
                    for k in range(j):
                        my_list_column[k].pop()
                    break

            # If the limit is not reached, move to the next row
            if check == False:
                break

    # Fill the Sudoku game board with random numbers from my_list
    for i in range(9):
        random_number = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        for _ in range(7):
            x = random.choice(random_number)
            my_game[i][x] = my_list[i][x]
            random_number.remove(x)

    # Return the generated Sudoku board
    return my_list
