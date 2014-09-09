
# PROTOTYPE
# Responsible for procedurally generated maps

import random
import textgen

class Map:
    """Each text adventure is played out on a single map, which is just a 2D grid of Locations.
       Locations can be linked to each other if they are adjacent in one of the four cardinal directions (n,s,w,e)."""
       
    def __init__(self, width, height):
        self.grid  = [[Location() for i in range(width)] for i in range(height)]
        
        # Record each Location's grid coordinates 
        for i in range(width):
            for j in range(height):
                location = self.grid[i][j]
                location.x = i
                location.y = j
        
        self.width = width
        self.height = height
        
        self.start_location = None
        self.end_location = None
        self.farthest_location = None
        self.attributes = []
        
        # self.leafs # Locations with only 1 connection out
        # self.halls # Locations with 2 connections out that are opposite directions
        # self.turns # Locations with 2 connections out that are not opposite directions
        # self.intersections # Locations with 3 or more connections out
        
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

# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  
            
class Location:
    """Represents a single room or area in a map."""
    def __init__(self):
        self.name  = None
        self.description = None
        self.attributes = []        
        
        self.x = -1
        self.y = -1
        
        self.n = None
        self.s = None
        self.e = None
        self.w = None

    def edge_count(self):
        sum = 0
        if self.n:
            sum += 1
        if self.s:
            sum += 1
        if self.e:
            sum += 1
        if self.w:
            sum += 1
        return sum

    def is_leaf(self):
        return self.edge_count() == 1

# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  


# True iff the given coordinates exist on the specified map
def is_valid(map, x, y):  
    if x < 0 or y < 0 or x >= map.width or y >= map.height: 
        return False
    else:
        return True

# True iff the Location at the specified coordinates is 'unvisited'
# (in the context of search algorithms). Unvisited Locations still
# have names defined as None
def is_visited(map, x, y):    
    return map.get(x, y) and map.get(x, y).name != None

# Returns the total number of adjacent (n,s,w,e directions only) Locations that have been visited.
# (in the context of search algorithms). Used to control sparseness of connected Rooms.
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

    
# Introduces most of a map's main layout by recursively connecting Locations
# together using randomized depth-first search. It enforces sparseness when
# connecting rooms. This function is recursive.
def connect_recursively_sparse(map, x, y, previous_x, previous_y, current_depth):

    if not is_valid(map, x, y): 
        return
    if is_visited(map, x, y):
        return
        
    # This has an impact on density. Choose a number from 1-4 inclusive. The higher the number, the more dense the map.
    if visited_neighbour_count(map, x, y) > 1: 
        return
           
    # Mark as visited, connect to the previous Location, and update the Location furthest from the starting location
    current_location = map.get(x,y)
    current_location.name = "Visited"
    current_location.depth = current_depth
    
    if not map.farthest_location or current_location.depth > map.farthest_location.depth:
        map.farthest_location = current_location
    
    if previous_x != None and previous_y != None:
        map.connect(x,y,previous_x,previous_y)
    
    # Randomly proceed to an adjacent, unvisited location
    places = []
    for i in range(-1,2,2): # -1, 1 only
        if is_valid(map, x+i, y):
            places.append(map.get(x+i,y))
            
        if is_valid(map, x, y+i):
            places.append(map.get(x,y+i))
    
    while len(places) > 0:
        next_location = places.pop(random.randint(0,len(places)-1))
        connect_recursively_sparse(map, next_location.x, next_location.y, x, y, current_depth + 1)

# Given a single Location on a map, this function will
# choose a random, unvisited, adjacent, second Location
# and connect the pair.
def connect_single_adjacent(map, x, y):
    if not is_valid(map, x, y): 
        return
    if not is_visited(map, x, y):
        return
    
    places = []
    for i in range(-1,2,2): # -1, 1 only
        if is_valid(map, x+i, y):
            places.append(map.get(x+i,y))
            
        if is_valid(map, x, y+i):
            places.append(map.get(x,y+i))
    
    while len(places) > 0:
        next_location = places.pop(random.randint(0,len(places)-1))
        next_x = next_location.x
        next_y = next_location.y
        
        if is_valid(map, next_x, next_y) and not is_visited(map, next_x, next_y):
            next_location.name = "Visited"
            next_location.depth = map.get(x,y).depth + 1
            map.connect(x, y, next_x, next_y)
            break

# Adds attributes to the room which can have an affect
# on items, events, descriptions, etc
def generate_attributes(map, x, y):
    
    new_attributes = []
    location = map.get(x,y)
    edges = location.edge_count()
    
    
    # Physical attributes
    if edges == 1:
        new_attributes.append('leaf')
    elif edges == 2 and ((location.n and location.s) or (location.w and location.e)):
        new_attributes.append('hall')
    elif edges == 2:
        new_attributes.append('turn')
    else:
        new_attributes.append('intersection')
    
    # Lighting
    if random.random() < 0.33:
        new_attributes.append('dark')
    else:
        new_attributes.append('bright')
    
    # Atmospheric attributes
    if random.random() < 0.2:
        new_attributes.append('positive')
    else:
        new_attributes.append('negative')
        
    # Items
    if random.random() < 0.5:
        new_attributes.append('common_item')
    elif random.random() < 0.7:
        new_attributes.append('special_item')
    
    return new_attributes
            
# Generates an adventure map using a randomized version of the depth-first search algorithm
def create_dfs_map(width, height):

    map = Map(width, height)
    start_x, start_y = 3, 3
    
    connect_recursively_sparse(map, start_x, start_y, None, None, 0)
    
    map.starting_location = map.get(start_x,start_y)
    map.starting_location.attributes += ['start']
    
    map.ending_location = map.farthest_location
    map.ending_location.attributes += ['end']
    
    for i in range(0,3):
        connect_single_adjacent(map, start_x, start_y)

    for i in range(map.width):
        for j in range(map.height):
            location = map.get(i, j)
            if location != map.ending_location and random.random() < 0.25:
                connect_single_adjacent(map, i, j)
    
    for i in range(map.width):
        for j in range(map.height):
            location = map.get(i, j)
            location.attributes += generate_attributes(map, i, j)
            location.description = textgen.describe(location)  
    
    return map
