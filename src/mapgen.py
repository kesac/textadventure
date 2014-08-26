
# Responsible for procedurally generated maps

class Location:
    """Represents a location in a 2-dimensional map grid."""
    def __init__(self):
        self.name  = None
        self.description = None
        self.n = None
        self.s = None
        self.e = None
        self.w = None

def create_dfs_map(width, height):
    """Generates an adventure map using a randomized version of the depth-first search algorithm"""
    
    grid = [[Location() for i in range(width)] for i in range(height)]
    
    def is_valid(grid,x,y):
        if x < 0 or y < 0 or x >= len(grid) or x>= len(grid[0]): # Valid only if it exists on the grid?
            return False
        else:
            return True

    def neighbour_count(grid,x,y):
        sum = 0
        if is_valid(grid,x + 1,y) and grid[x + 1][y].name != None:
            sum += 1
        if is_valid(grid,x - 1,y) and grid[x - 1][y].name != None:
            sum += 1
        if is_valid(grid,x,y + 1) and grid[x][y + 1].name != None:
            sum += 1
        if is_valid(grid,x,y - 1) and grid[x][y - 1].name != None:
            sum += 1
        return sum
            
    def dfs(grid,x,y):

        if not is_valid(grid,x,y):
            return
        elif neighbour_count(grid,x,y) > 2:
            return

        grid[x][y].name = "A place"
               
        dfs(grid,x-1,y)       
        #dfs(grid,x+1,y)
        #dfs(grid,x,y+1)
        dfs(grid,x,y-1)
        
    #grid[5][5].name = "valid"
    dfs(grid,5,5)
    return grid
    
    