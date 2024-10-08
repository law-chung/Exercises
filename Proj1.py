# Project 1: Adventure game
# Checkpoint 1 due Sept. 26, final version due Oct. 10. 

# open the text file into program
gamefile = open('game1.txt')

# numpy for matrix 
import numpy as np 

# init game info and map dictionaries
gameinfo = {}
mapdict = {}
npc_dict = {}

# build a dictionary containing game info
def gamebuild(gamefile):
    current_r = 0 # current room counter
    for line in gamefile:
        line = line.rstrip()
        if line != '---':
            lineparts = line.split(':')
            # following lines from in class example
            k = lineparts[0]
            v = lineparts[1].lstrip()
            if 'game_' in lineparts[0]:
                k1, k2 = k.split('_')
                gameinfo[k2] = v
                # end class example
            # adding room id to mapdict key and creating dict within dict of elements under the room id 
            if 'r_id' in lineparts[0]:
                mapdict[lineparts[1]] = {'desc': '', 'id': str(lineparts[1]),'obj': []}
                current_r += 1 # adds to current_r counter 
            # adds description to current room index dict 
            if 'r_desc' in lineparts[0]:
                mapdict[str(current_r)]['desc'] = lineparts[1][1:] # 1: is to remove the space at the start of the string
            # adds object to current room object list
            if 'r_obj' in lineparts[0]:
                mapdict[str(current_r)]['obj'].append(lineparts[1][1:])
            # creates hiddenobj key under current room dict and adds the object. Stores as string b/c 1 hidden obj per room max.
            if 'r_hiddenobj' in lineparts[0]:
                mapdict[str(current_r)]['hiddenobj'] = lineparts[1][1:]
            # creates hiddenpath key under current room dict and adds the path destination 
            if 'r_hiddenpath' in lineparts[0]:
                mapdict[str(current_r)]['hiddenpath'] = lineparts[1]
            # next 4 if statements add movement overrides if found
            if 'r_north' in lineparts[0]:
                mapdict[str(current_r)]['north'] = lineparts[1]
            if 'r_east' in lineparts[0]:
                mapdict[str(current_r)]['east'] = lineparts[1]
            if 'r_south' in lineparts[0]:
                mapdict[str(current_r)]['south'] = lineparts[1]
            if 'r_west' in lineparts[0]:
                mapdict[str(current_r)]['west'] = lineparts[1]
            # npc dictionary creation 
            if 'npc_' in lineparts[0]: 
                k1, k2 = k.split('_', maxsplit = 1) # ex: k1 = npc_,  k2 = timmytarheel_1
                k3, k4 = k2.split('_') # ex: k3 = npc name, k4= speech number
                if k3 not in npc_dict: # if npc name is not a key in npcdict yet
                    npc_dict[k3] = {k4: v, 'count': 0} # add npc name as a key, populate with key value pairs for talking and 0-indexed counter key value pair
                else:
                    npc_dict[k3][k4] = v # create npc name and location pairing

    return gameinfo, mapdict

# build game 
gamebuild(gamefile)


# class that will enable user inputs and map movement
class Movement:
    # init - will require gamemap x and y, and mapdict for the game. 
    def __init__(self, x, y, mapdict):
        self.mapdict = mapdict
        self.x = x # map width
        self.y = y # map height
    # movement function
    def move(self, direction):
        global player_position # takes in player position global - ensures player position is always updated 
        current_x, current_y = self.get_coord(player_position) # calls get coordinate function to source current x and y 
        # check for movement overrides
        if str(player_position) in mapdict and direction in self.mapdict[str(player_position)]:
            new_position = int(self.mapdict[str(player_position)][direction])
            player_position = new_position
        # normal movement
        else:
            if direction == 'north':
                current_y = (current_y - 1) % self.y # subtracts from current y (0 is at the top of the map) and modulo by map size y to check if on edge
            elif direction == 'south':
                current_y = (current_y + 1) % self.y # adds to current y and mod to check edge 
            elif direction == 'west':
                current_x = (current_x - 1) % self.x # subtracts from current x - left side is 0. mod to check edge
            elif direction == 'east':
                current_x = (current_x + 1) % self.x # adds to current x. mod to check edge
            else:
                print("Invalid direction!") # feedback for inputs that aren't listed 
                return
            player_position = self.get_position(current_x, current_y) # update position 
        # prints message to player with current position description
        print(f"You are {mapdict[str(player_position)]['desc']}")
        if mapdict[str(player_position)]['obj'] != []: # if obj list in mapdict is not empty
            print(f"There is a {mapdict[str(player_position)]['obj'][0]} here.") # print first indexed obj
    # get coordinate function - takes in position arg
    def get_coord(self, position):
        position -= 1 # 0-indexed
        x = position % self.x # position modulo map x - gives column the player is on 
        y = position // self.x # position divided by map x - gives row the player is on 
        return x, y
    # get position function
    def get_position(self, x, y): # takes in x and y 
        return y * self.x + x + 1 # returns y * mapx and adds x +1 

# set game run variable for use below
move = Movement(int(gameinfo['xsize']), int(gameinfo['ysize']), mapdict)

# init inventory and starting location
player_position = int(gameinfo['start'])
inv = []

# Print welcome message to the game 
print('')
print(f"Welcome to {gameinfo['name']}! Good luck, traveler.")
print('')
print(f"Your goal is to {gameinfo['goal'].lower()}")
print('')
print(f"You are {mapdict[str(player_position)]['desc']}")

# 
while True:
    print('')
    # checks to see if goal is reached - goal object is in goallocation's obj list
    if gameinfo['goalobj'] in mapdict[str(gameinfo['goalloc'])]['obj']:
        print('Congratulations! You have won the game. Thanks for playing!')
        break
    cmd = input("What next? ") # prompt
    if cmd == 'exit': # exit game command
        break
    else: # if not a command from above, proceed to the following code. 
        if cmd == "inv": # inv command
            print(f"Your inventory: {inv}") # print inventory
        elif cmd == "goal": # check goal command
            print(gameinfo['goal']) # print goal
        elif cmd == "search": # search command
            if 'hiddenobj' in mapdict[str(player_position)]: # checks if hidden obj is in dict for current room
                print(f"You found a {mapdict[str(player_position)]['hiddenobj']}") # prints message to player
            elif 'hiddenpath' in mapdict[str(player_position)].keys(): # checks if hiddenpath is in keys for current room
                print("You found a hidden path!") # prints that hidden path was found 
            else: # if no hidden things are found print message
                print('Nothing found!')
        elif cmd == "move path": # move along hidden path
            if 'hiddenpath' in mapdict[str(player_position)]: # if there is a hidden path
                player_position = int(mapdict[str(player_position)]['hiddenpath'])
                print(f"You are {mapdict[str(player_position)]['desc']}")
            else: # no path message
                print('No paths!')
        elif cmd == "check location": # print current position
            print(player_position)
        # taking and dropping objects 
        elif 'take' in cmd or 'drop' in cmd: # if either take or drop is submitted 
            # split the input in 2 
            cmd_parts = cmd.split() # default split by space 
            c1 = cmd_parts[0]
            c2 = cmd_parts[1]
            if c1 == 'take': # if taking
                # if c2 is in current room obj list
                if c2 in mapdict[str(player_position)]['obj']:
                    print(f"Added {mapdict[str(player_position)]['obj'][0]}") # print msg
                    inv.append(mapdict[str(player_position)]['obj'][0]) # add first indexed obj to inventory
                    del mapdict[str(player_position)]['obj'][0] # remove first indexed obj from room 
                elif 'hiddenobj' in mapdict[str(player_position)]:
                    if c2 in mapdict[str(player_position)]['hiddenobj']:
                        print(f"Added {mapdict[str(player_position)]['hiddenobj']}")
                        inv.append(mapdict[str(player_position)]['hiddenobj'])
                        del mapdict[str(player_position)]['hiddenobj']
                else:
                    print(f"Can't take {c2}!")
            elif c1 == 'drop':
                if c2 in inv:
                    print(f"Dropped {c2}")
                    mapdict[str(player_position)]['obj'].append(c2)
                    inv.remove(c2)
                else:
                    print(f"Can't drop {c2}!")
        elif 'move' in cmd:
            cmd_parts = cmd.split()
            c1 = cmd_parts[0]
            c2 = cmd_parts[1]
            if c2 == 'north':
                move.move('north')
            elif c2 == 'south':
                move.move('south')
            elif c2 == 'west':
                move.move('west')
            elif c2 == 'east':
                move.move('east')
            else:
                print('Invalid direction!')
        elif 'talk' in cmd:
            cmd_parts = cmd.split()
            c1 = cmd_parts[0]
            c2 = cmd_parts[1]
            if c2 in npc_dict.keys():
                if str(player_position) == npc_dict[c2]['loc']:
                    if npc_dict[c2]['count'] + 2 < len(npc_dict[c2]):
                        print(npc_dict[c2][str(npc_dict[c2]['count'] + 1)])
                        npc_dict[c2]['count'] += 1
                    else:
                        print(npc_dict[c2][str(npc_dict[c2]['count'])])
                else:
                    pass
        