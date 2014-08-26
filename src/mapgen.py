


# Responsible for procedurally generated maps


import random

class Location:
    """Represents a location in a 2-dimensional map grid."""
    def __init__(self):
        self.name  = None
        self.description = None
                
        self.x = None
        self.y = None
        
        self.n = None
        self.s = None
        self.e = None
        self.w = None

def is_valid(grid,x,y):
    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]): # Valid only if it exists on the grid?
        return False
    else:
        return True

def is_visited(grid,x,y):
    return grid[x][y].name != None

def visited_neighbour_count(grid,x,y):
    sum = 0
    if is_valid(grid,x + 1,y) and is_visited(grid,x + 1,y):
        sum += 1
    if is_valid(grid,x - 1,y) and is_visited(grid,x - 1,y):
        sum += 1
    if is_valid(grid,x,y + 1) and is_visited(grid,x,y + 1):
        sum += 1
    if is_valid(grid,x,y - 1) and is_visited(grid,x,y - 1):
        sum += 1
    return sum
        
def create_dfs_map(width, height):
    """Generates an adventure map using a randomized version of the depth-first search algorithm"""
    
    grid = [[Location() for i in range(width)] for i in range(height)]
    
    i = 0
    j = 0
    for row in grid:
        j = 0
        for location in row:
            location.x = i
            location.y = j
            j += 1
        i += 1    

    def dfs(grid,x,y):

        if not is_valid(grid,x,y):
            return
        
        if is_visited(grid,x,y):
            return

        if visited_neighbour_count(grid,x,y) > 1:
            return
               
        # Otherwise, mark as visited
        grid[x][y].name = "A place"
        
        # Where should we go next?
        places = []
        
        if is_valid(grid,x-1,y):
            places.append(grid[x-1][y])

        if is_valid(grid,x,y-1):
            places.append(grid[x][y-1])
            
        if is_valid(grid,x+1,y):
            places.append(grid[x+1][y])

        if is_valid(grid,x,y+1):
            places.append(grid[x][y+1])
        
        while len(places) > 0:
            next_location = places.pop(random.randint(0,len(places)-1))
            dfs(grid,next_location.x,next_location.y)

    dfs(grid,0,0)
    return grid
    
    