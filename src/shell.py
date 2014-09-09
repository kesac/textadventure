
# PROTOTYPE
# Interactive shell the player uses to play the game

import os
import textwrap

def start(map):

    player_location = map.starting_location
    
    # you are currently in a...
    # you can move...
    command = None
    last_location = None
    
    valid_command = True
    valid_move = False
    
    while command != 'exit':
    
        if not valid_command: 
            print('I am not sure what you mean by that')
            valid_command = True;
        else:        
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
                
            if last_location:
                print('You came from', last_location)
    
        command = input(" > ")
        
        valid_move = False
        valid_command = False
        
        if command == 'n':
            valid_command = True
            if player_location.n:
                player_location = player_location.n
                last_location = 's'
                valid_move = True
            
        if command == 's':
            valid_command = True
            if player_location.s:
                player_location = player_location.s
                last_location = 'n'
                valid_move = True
                
        if command == 'w':
            valid_command = True
            if player_location.w:
                player_location = player_location.w
                last_location = 'e'
                valid_move = True

        if command == 'e':
            valid_command = True
            if player_location.e:
                player_location = player_location.e
                last_location = 'w'
                valid_move = True
                
    