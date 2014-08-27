
# PROTOTYPE
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
    """Valid only if the given coordinates exist on the specified grid (2D array)"""
    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]): 
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

def is_connected(edges,x,y,x2,y2):
    return '%s,%s->%s,%s' % (x, y, x2, y2) in edges
    
def create_dfs_map(width, height):
    """Generates an adventure map using a randomized version of the depth-first search algorithm"""
    
    grid  = [[Location() for i in range(width)] for i in range(height)]
    edges = {}
    
    # Record each location's grid coordinates 
    i,j = 0,0
    for row in grid:
        j = 0
        for location in row:
            location.x = i
            location.y = j
            j += 1
        i += 1    

    # Start generating the map by depth-first search exploration
    def dfs(grid, x, y, prev_x, prev_y):

        if not is_valid(grid, x, y):
            return
        if is_visited(grid, x, y):
            return
        if visited_neighbour_count(grid, x, y) > 1:
            return
               
        # Otherwise, mark as visited
        grid[x][y].name = "Visited"
        
        if prev_x != None and prev_y != None:
            edges['%s,%s->%s,%s' % (x, y, prev_x, prev_y)] = True
            edges['%s,%s->%s,%s' % (prev_x, prev_y, x, y)] = True
        
        # Where should we go next?
        places = []
        
        if is_valid(grid, x-1 ,y):
            places.append(grid[x-1][y])

        if is_valid(grid, x, y-1):
            places.append(grid[x][y-1])
            
        if is_valid(grid, x+1, y):
            places.append(grid[x+1][y])

        if is_valid(grid, x, y+1):
            places.append(grid[x][y+1])
        
        while len(places) > 0:
            next_location = places.pop(random.randint(0,len(places)-1))
            dfs(grid, next_location.x, next_location.y, x, y)

    dfs(grid, 0, 0, None, None)
        
    # Fill the connections out
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            
            if is_valid(grid, x-1, y) and is_connected(edges, x, y, x-1, y):
                grid[x][y].w = grid[x-1][y]
                grid[x-1][y].e = grid[x][y]
            
            if is_valid(grid, x, y-1) and is_connected(edges, x, y, x, y-1):
                grid[x][y].n = grid[x][y-1]
                grid[x][y-1].s = grid[x][y]
            
            if is_valid(grid, x+1, y) and is_connected(edges, x, y, x+1, y):
                grid[x][y].e = grid[x+1][y]
                grid[x+1][y].w = grid[x][y]
                
            if is_valid(grid, x, y+1) and is_connected(edges, x, y, x, y+1):
                grid[x][y].s = grid[x][y+1]
                grid[x][y+1].w = grid[x][y]

        
            
    return grid
    
#---------------------------------