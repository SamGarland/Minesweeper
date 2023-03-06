# This programme consists of (1) a function called minesweeper, (2) a grid  and (3) a function call
# (1) The function takes a grid (2) and outputs a numbered grid, where the number of each space relates
# to the adjacent "#" spaces.

#---- Minesweeper ----#
# 1)
def minesweeper(grid):
    
    # This finds out how many rows and collumns the grid has.
    
    num_rows = 0
    num_cols = 0
    
    for row in grid:
       num_rows += 1
        
    for row in grid:
       for col in range(len(row)):
          num_cols += 1
            
    num_cols = int(num_cols/num_rows)
    num_rows = num_rows
    
    # This numbers the "-" spaces as 0.

    for row in range(len(grid)):
        for col in range(len(grid)):
            if grid[row][col] == "-":
                grid[row][col] = 0
    
    # This checks whether each space of the grid is "#", and if so skips it.
    # Otherwise it checks the surrounding spaces for "#" (mines) and calculates the number of the space
    # The if statements are bounded within certain sections of the grid to avoid going outside the grid e.g. "col > 0".
    
    for row in range(len(grid)):
        for col in range(len(grid)):
            # if it's a mine then continue
            if grid[row][col] == "#":
                continue
            #check left
            if col > 0 and grid[row][col - 1] == "#":
                grid[row][col] += 1
            #check right
            if col < (num_cols - 1) and grid[row][col + 1] == "#":
                grid[row][col] += 1
            #check above
            if row > 0 and grid[row - 1][col] == "#":
                grid[row][col] += 1
            #check below
            if row < (num_rows - 1) and grid[row + 1][col] == "#":
                grid[row][col] += 1
            #check top left
            if col > 0 and row > 0 and grid[row - 1][col - 1] == "#":
                grid[row][col] += 1
            #check top right
            if col < (num_cols - 1) and row > 0 and grid[row - 1][col + 1] == "#":
                grid[row][col] += 1
            #check bottom left
            if row < (num_rows - 1) and col > 0 and grid[row + 1][col + -1] == "#":
                grid[row][col] += 1
            #check bottom right
            if row < (num_rows - 1) and col < (num_cols - 1) and grid[row + 1][col + 1] == "#":
                grid[row][col] += 1
    
    # This prints the new numbered grid. 
        
    for line in grid:
        print(line)               
                
# 2)                
grid = [["-", "-", "-", "#", "#"], 
        ["-", "#", "-", "-", "-"], 
        ["-", "-", "#", "-", "-"], 
        ["-", "#", "#", "-", "-"], 
        ["-", "-", "-", "-", "-"]]                
# 3)
minesweeper(grid)             
                
                
                
                
                
                
                
                
                
                
                
                
