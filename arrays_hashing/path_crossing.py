"""
PROBLEM:
- we are given a string which denotes a path
- letters in string are N S E W each denoting a direction
- each letter means moving one unit of distance in that direction 
- we need to return true if the path ever crosses itself
- if the path doesn't cross itself, we return false

EXAMPLES:
path = NES (North East South)
output = False

path = NESWW
output = False

EDGE CASES:
string will always be greater than 1
string will always only have NSEW

APPROACH:
N gets cancelled by S
S gets cancelled by N
E gets cancelled by W
W gets cancelled by e

path can cross itself at any point, doesn't have to be point 0
we can keep track of locations as we start travelling
after each move, we can check whether we have travelled to this location before
as we always start at location (0, 0)
first zero can mean distance at NE axis and second 0 can mean the distance at SW axis
every time we move we add or subtract accordingly to the related axis
N +1
S -1
E +1
W -1

PSEUDO CODE:
DEF is_path_crossing(path): #NES
    cur_location = [0, 0]
    path_locations = [cur_location]

    for direction in path:
        cur_location[0] += direction == 'N'
        cur_location[0] -= direction == 'S'
        cur_location[1] += direction == 'E'
        cur_location[1] -= direction == 'W'

        if cur_loction in path_locations:
            return True
        path_locations.append(cur_location)

    return False
"""
def is_path_crossing(path):
    cur_location = [0, 0]
    path_locations = [cur_location[:]]

    for direction in path:
        cur_location[0] += direction == 'N'
        cur_location[0] -= direction == 'S'
        cur_location[1] += direction == 'E'
        cur_location[1] -= direction == 'W'

        if cur_location in path_locations:
            return True
        path_locations.append(cur_location[:])
    
    return False

print(is_path_crossing('NNEESSWW'))

# A slightly optimized solution
def is_path_crossing(path):
    cur_location = (0, 0)
    path_locations = {cur_location}

    for direction in path:
        x, y = cur_location
        x += direction == 'N'
        x -= direction == 'S'
        y += direction == 'E'
        y -= direction == 'W'
        cur_location = (x, y)

        if cur_location in path_locations:
            return True
        path_locations.add(cur_location)
    
    return False

# From O(n*n) to O(n) becuase lookup in a hash set is O(1) unlike in a list
# where it is O(n)
         