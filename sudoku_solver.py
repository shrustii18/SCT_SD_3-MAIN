def find_empty_location(grid):
    """
    Finds an empty cell (represented by 0) in the Sudoku grid.
    Returns the row and column indices as a tuple (row, col) if found, otherwise None.
    """
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return (row, col)  # Row, Col
    return None

def is_valid(grid, num, pos):
    """
    Checks if placing a number in a given position is valid according to Sudoku rules.
    :param grid: The Sudoku grid (9x9 list of lists).
    :param num: The number to be placed.
    :param pos: A tuple (row, col) representing the position to place the number.
    :return: True if the placement is valid, False otherwise.
    """

    # Check row
    for i in range(9):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(9):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False

    # Check 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if grid[i][j] == num and (i,j) != pos:
                return False

    return True

def solve_sudoku(grid):
    """
    Solves a Sudoku puzzle using backtracking.
    :param grid: The Sudoku grid (9x9 list of lists) to be solved.
    :return: True if the puzzle is solved successfully, False otherwise.
    """

    find = find_empty_location(grid)
    if not find:
        return True  # No empty spaces left, puzzle is solved
    else:
        row, col = find

    for num in range(1,10):
        if is_valid(grid, num, (row, col)):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True

            grid[row][col] = 0  # Backtrack: reset the cell to 0

    return False  # No valid number found, trigger backtracking

def print_grid(grid):
    """
    Prints the Sudoku grid in a readable format.
    """
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")

# Example Sudoku puzzle (0 represents empty cells)
example_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Unsolved Sudoku:")
print_grid(example_grid)

if solve_sudoku(example_grid):
    print("\nSolved Sudoku:")
    print_grid(example_grid)
else:
    print("\nNo solution exists")
