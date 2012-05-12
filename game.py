current_section = 0

# game sections
sections = [
    ("""You are in the island port. Behind you is the boat that brought you here. Facing south, further down is an abandoned tower. There is a house on on your west.""", 
     "Island dock"), #0
    ("""On your left is a house. Northeast is an abandoned tower. Further east is another house.""",
     "Western beach"), #1
    ("""On your south is the great south sea. Beside you is a cave. East you can what seems to be a ceremonial site.""",
     "The Cave grounds"), #2
    ("""In front of you is a small chapel. Looking south, you can see a cave opening. Northwest there is a tower.""",
     "The Chapel grounds"), #3

    ("""You are in an open field with a really huge tree in the middle. On your west is a tower. South there's a church. Facing east is a small house. Northeast is the Town Hall""",
     "Sommerset road"), #4
    ("""You are standing in front of the town hall. On the south is a small house.""",
     "The Town Hall Grounds"), #5
    ("""All around you are unmarked graveyards. North is a small house. West is the small church. Southwest is a cave opening. South is what seems to be a ceremonial site""",
     "The Graveyard"), #6
    ("""Before you is what seems to be a ceremonial site of an unknown belief system. To your west is a cave opening. North is the graveyard""",
     "The Ceremonial Site"), #7

    ("""Beside you is a small house. To your north is the open sea, and northeast is the island dock. Souteast is a tower.""",
     "Northwestern Beach"), #8
    ("""To your west is the island dock. On the east is the Town hall. Southwest is a big tower, and down south sits and even bigger tree.""",
     "Northern beach"), #9
    ("""To your north is a small house. On the east is a tower. Northeast is the island docks. Down south is another small house""",
     "Cuttercrow fields"), #10
    ("""In front of you is a tower that looks abandoned. To your north is the island docks, with a small house on the northeast. To the east is a field with a really huge tree in the middle. South east is the island church.""",
     "The Tower grounds"), #11

    ("""Beside you is a small house. To your north is the Town Hall. On the west is a field with a gargantuan tree in the middle. Southwest is the island church. On the south is a graveyard.""",
     "Eastern Beach"), #12
    ("""On the west is a small house. North is a huge tower. Northeast is a large tree in the middle of a field. On the east is the island church. Southeast is a cave opening.""",
     "Ledore road"), #13
    ("""You are in the middle of a smelly and dark marsh. To your north is a small house. On the south and southwest is the open sea.""",
     "Maplehide marshes"), #14
    ("""On the south is the open sea. Northwest is a small house. Northeast is the town church. On the east is a cave opening.""",
     "Huntington beach"), #15

    # rooms
    ("""You are inside a worn down house. The name 'Rindley' is marked on the table.""",
     "Rindley's house"), #16
    ("""You are inside a huge abandoned hall. Cobwebs all over. Except for some turned tables and wrecked cabinets, the hall seems empty""",
     "Town Hall"), #17
    ("""You are inside an empty tower. There is a stair that leads to the top. You can climb the stairs if you want to""",
     "The Tower"), #18
    ("""You are now on top of the tower. The stair that leads down is also before you.""",
     "The Tower top"), #19

    ("""You are inside a nice looking house, almost as if it is being inhabited if not for the cobwebs all over. On the door is marked the name 'Milton'. There is a ben on the right side of the room.""",
     "Milton's house"), #20
    ("""You are inside a house that has weeds growing inside. A portrait hangs in the room, but the face is unrecognizable due to tear. The name Feldon is written below the portrait.""",
     "Feldon's house"), #21
    ("""You are inside a house turned church that reeks with dust and weeds growing all over. A cross is seen in the front, indicating that this must have been built by missionaries.""",
     "The Chapel"), #22
    ("""You are inside a cave. The path further down seems to have been blocked by a cave in.""",
     "The Cave"), #23
]

# game sections shorthand
sec = {}
for indexed in enumerate(sections):
    index = indexed[0]
    long_name = indexed[1][1] # indexed[1][0] is the description
    short_name = ''
    for C in long_name:
        if C in ' /': # spaces and slashes to dashes
            short_name += '-'
        elif not C in ".'": # don't use periods and apostrophes
            short_name += C.lower() # lowercase
    sec[short_name] = index

# game directions
dirs = {'north': 0, 'n': 0, 'south': 1, 's': 1,
        'west': 2, 'w': 2, 'east': 3, 'e': 3,
        'northeast': 4, 'ne': 4, 'southeast': 5, 'se': 5,
        'northwest': 6, 'nw': 6, 'southwest': 7, 'sw': 7,
        'up': 8, 'u': 8, 'down': 9, 'd': 9,
        'in': 10, 'out': 11, 'on': 10, 'off': 11,
        'enter': 10, 'exit': 11}

island_map = [
#      n   s   e   w  ne  nw  se  sw  up  dn  in  out
    [ -1, 10,  0, -1, -1, -1, 11, -1, -1, -1, -1, -1], #0
    [ -1, 11,  8, -9, -1, -1, 10,  4, -1, -1, 21, -1], #1
    [ -1,  4,  5,  0, -1, -1, 12, 11, -1, -1, 23, -1], #2
    [ -1, 12, -1,  9, -1, -1, -1,  4, -1, -1, 22, -1], #3
    
    [  8,  1, 11, -1,  0, -1, 13, -1, -1, -1, -1, -1], #4
    [  0, 13,  4, 10,  9,  8,  3,  1, -1, -1, 17, -1], #5
    [  9,  3, 12,  5,  5,  0,  6, 13, -1, -1, -1, -1], #6
    [  5,  6, -1,  4, -1,  9, -1,  3, -1, -1, -1, -1], #7
    
    [ 10, 14, 13, -1, 11, -1, 15, -1, -1, -1, 16, -1], #8
    [ 11, 15,  3,  1,  4, 10,  2, 14, -1, -1, -1, -1], #9
    [  4,  2,  6, 13, 12, 11,  7, 15, -1, -1, -1, -1], #10
    [ 12,  7, -1,  3, -1,  4, -1,  2, -1, -1, 18, -1], #11
    
    [  1, -1, 15, -1, 13, -1, -1, -1, -1, -1, 20, -1], #12
    [ 13, -1,  2, 14,  3,  1, -1, -1, -1, -1, -1, -1], #13
    [  3, -1,  7, 15,  6, 13, -1, -1, -1, -1, -1, -1], #14
    [  6, -1, -1,  2, -1,  3, -1, -1, -1, -1, -1, -1], #15

    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  8], #16
    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  5], #17
    [ -1, -1, -1, -1, -1, -1, -1, -1, 19, -1, -1, 11], #18
    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, 18, -1, -1], #19

    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12], #20
    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  1], #21
    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  3], #22
    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  2], #23
]

# game objects
obj = {
    # takable objects
    'shovel': 0,
    'lamp': 1,
    'sword': 2,
    
    # permanent objects
    'bed': -1,
}

# takable object descriptions
tk_objs = [
    ("There is a shovel for digging here.", "A shovel"),
    ("There is a shiny brass lamp nearby.", "A brass lantern"),
    ("There is a sharp sword on the ground.", "A sharp sword"),
]

# permanent object descriptions
perm_obj_desc = [
    None,
    "A bed with the perfect mattress for sleep.",
]

inventory = [-1]
items = {
0: [],
1: [],
2: [],
3: [obj['sword']],
4: [],
5: [],
6: [],
7: [],
8: [],
9: [],
10: [],
11: [obj['lamp']],
12: [obj['bed']],
13: [],
14: [],
15: [obj['shovel']],
}
