def print_grid(grid):
    """Function to print the Sudoku grid."""
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def is_valid(grid, row, col, num):
    """Check if it's valid to place a number in the given cell."""
    
    for x in range(9):
        if grid[row][x] == num:
            return False
    
    
    for x in range(9):
        if grid[x][col] == num:
            return False
    
    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False
    
    return True

def solve_sudoku(grid):
    """Solve the Sudoku puzzle using backtracking."""
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0: 
                for num in range(1, 10):  
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):  
                            return True
                        grid[row][col] = 0  
                return False  
    return True  

if __name__ == "__main__":
    
    sudoku_grid = [
        [3, 0, 0, 8, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 1, 0, 5, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 4, 1, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    print("Original Sudoku Grid:")
    print_grid(sudoku_grid)

    if solve_sudoku(sudoku_grid):
        print("\nSolved Sudoku Grid:")
        print_grid(sudoku_grid)
    else:
        print("No solution exists.")
