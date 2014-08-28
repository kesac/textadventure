
# PROTOTYPE
# Responsible for procedurally generated maps

import random

class Map:
    """Each text adventure is played out on a single map, which is just a 2D grid of Locations.
       Locations can be linked to each other if they are adjacent in one of the four cardinal directions (n,s,w,e)."""
       
    def __init__(self, width, height):
        self.grid  = [[Location() for i in range(width)] for i in range(height)]
        
        # Table of strings describing edges between Location pairs
        self.width = width
        self.height = height
        
        # self.start_location
        # self.end_location
        # self.farthest_location
        # self.leafs
        
    def get(self, x,y):
        return self.grid[x][y]
    
    # Behaviour when connecting two Locations that are not adjacent in one of
    # the four cardinal directions is undefined.
    def connect(self, x1,y1,x2,y2):
        if x1 < x2:
            self.grid[x1][y1].e = self.grid[x2][y2]
            self.grid[x2][y2].w = self.grid[x1][y1]
        elif x1 > x2:
            self.grid[x1][y1].w = self.grid[x2][y2]
            self.grid[x2][y2].e = self.grid[x1][y1]
        elif y1 < y2:
            self.grid[x1][y1].s = self.grid[x2][y2]
            self.grid[x2][y2].n = self.grid[x1][y1]
        elif y1 > y2:
            self.grid[x1][y1].n = self.grid[x2][y2]
            self.grid[x2][y2].s = self.grid[x1][y1]

class Location:
    """Represents a single room or area in a map."""
    def __init__(self):
        self.name  = None
        self.description = None
                
        self.x = -1
        self.y = -1
        
        self.n = None
        self.s = None
        self.e = None
        self.w = None

# Valid only if the given coordinates exist on the specified grid (2D array)
def is_valid(map, x, y):  
    if x < 0 or y < 0 or x >= map.width or y >= map.height: 
        return False
    else:
        return True

# It is assumed that unvisited locations do not have a name.
def is_visited(map, x, y):    
    return map.get(x, y) and map.get(x, y).name != None

# Returns the total of neighbouring (n,s,w,e directions only) locations that have been visited.
# Used to control sparseness of a generated map.
def visited_neighbour_count(map, x, y):
    sum = 0
    if is_valid(map, x + 1, y) and is_visited(map, x + 1, y):
        sum += 1
    if is_valid(map, x - 1, y) and is_visited(map, x - 1, y):
        sum += 1
    if is_valid(map, x, y + 1) and is_visited(map, x, y + 1):
        sum += 1
    if is_valid(map, x, y - 1) and is_visited(map, x, y - 1):
        sum += 1
    return sum
    
def create_dfs_map(width, height):
    """Generates an adventure map using a randomized version of the depth-first search algorithm"""

    map = Map(width, height)
    
    # Record each Location's grid coordinates 
    for i in range(map.width):
        for j in range(map.height):
            location = map.get(i, j)
            location.x = i
            location.y = j

    # Start generating the map by depth-first search exploration
    def dfs(map, x, y, prev_x, prev_y):

        if not is_valid(map, x, y): 
            return
        if is_visited(map, x, y):
            return
            
        # This has an impact on density. Choose a number from 1-4 inclusive. The higher the number, the more dense the map.
        if visited_neighbour_count(map, x, y) > 1: 
            return
               
        # If this is a valid, unvisited location, mark it as visited, and connect it to the previous Location
        map.get(x,y).name = "Visited"
        
        if prev_x != None and prev_y != None:
            map.connect(x,y,prev_x,prev_y)
        
        # Randomly proceed to an adjacent, unvisited location
        places = []
        for i in range(-1,2,2): # -1, 1 only
            if is_valid(map, x+i, y):
                places.append(map.get(x+i,y))
                
            if is_valid(map, x, y+i):
                places.append(map.get(x,y+i))
        
        while len(places) > 0:
            next_location = places.pop(random.randint(0,len(places)-1))
            dfs(map, next_location.x, next_location.y, x, y)

    dfs(map, 0, 0, None, None)

    return map
