import numpy as np

def string_to_array(sudoku_string):
    sudoku_list = [sudoku_string[i:i+4] for i in range(0, 16, 4)]
    sudoku_array = np.zeros((4, 4), dtype=int)

    for i, row in enumerate(sudoku_list):
        for j, char in enumerate(row):
            if char != ".":
                sudoku_array[i, j] = int(char)

    return sudoku_array

def categorize_columns(puzzle_array):
    columns = np.transpose(puzzle_array).tolist()
    
    return columns

def categorize_quadrants(puzzle_array):
    puzzle_array = np.array(puzzle_array).reshape(4, 4)
    quadrants = []

    for i in range(0, 4, 2):
        for j in range(0, 4, 2):
            quadrant = puzzle_array[i:i+2, j:j+2].flatten().tolist()
            quadrants.append(quadrant)

    return quadrants