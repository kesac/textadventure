
# PROTOTYPE
# Interactive shell the player uses to play the game

import textwrap

def start(map):

    player_location = map.starting_location
    
    # you are currently in a...
    # you can move...
    command = None
    
    while command != 'exit':
    
        header = 'You are currently in %s,%s' % (player_location.x, player_location.y)
        print("-" * len(header))
        print(textwrap.fill(header))
        print("-" * len(header))
        print(textwrap.fill(player_location.description))
        print("-" * len(header))
        print('You see exits to the [ ', end='')
        
        if player_location.n:
                print('n ', end='')
        if player_location.s:
                print('s ', end='')
        if player_location.w:
                print('w ', end='')
        if player_location.e:
                print('e ', end='')
        print(']')
    
        command = input(" > ")
        
        invalid_move = False
        if command == 'n':
            if player_location.n:
                player_location = player_location.n
            else:
                invalid_move = True
            
        if command == 's' and player_location.s:
            if player_location.s:
                player_location = player_location.s
            else:
                invalid_move = True
            
        if command == 'w' and player_location.w:
            if player_location.w:
                player_location = player_location.w
            else:
                invalid_move = True
            
        if command == 'e' and player_location.e:
            if player_location.e:
                player_location = player_location.e
            else:
                invalid_move = True
    