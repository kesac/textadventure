
import random


def get_basic_room_description(room):
    """A randomized, but very limited room description generator"""
    
    sizes = ["a small","an average","a large","a massive"]
    
    def get_room_size():
        return sizes[random.randint(0,len(sizes)-1)]

    def get_shape():
        # regular rectangular room
        
        if random.random() < 0.50:
            return "rectangular"
        else:
            return "irregular"
   
	# lighting
    def get_lighting():
        if random.random() < 0.33:
            return "There are torches on the walls, but none are lit. It is difficult to see other details inside the room."
        elif random.random() < 0.67:
            return "Multiple torches on every wall provide adequate lighting."
        else:
            return ""
	
	# points of interest in the room
    def get_points_of_interest():
        if random.random() < 0.33:
            return "There is an oak table in the middle of the room."
        elif random.random() < 0.67:
            return "There is a large painting of young woman with black hair on the wall. The eyes of the painting appear to have been scratched out."
        else:
            return ""
	
	# location of exits
    def get_exits():
        return "As far as you can tell, there are no exits or entrances to this room."
        
    description = [
        "You find yourself in %s, %s-shaped room." % (get_room_size(),get_shape()),
        " %s" % (get_points_of_interest()),
        " %s" % (get_lighting()),
        " %s" % (get_exits())
    ]

    return ''.join(description)

