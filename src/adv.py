from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

knife = Item("Knife", "Knife is a good tool to have")
net = Item("Net", "shield yourself from mosquitoes")
gin = Item("Gin", "drink some gin")

room["outside"].add_item([knife, net, gin])
room["outside"].get_item("Gin")

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Make a new player object that is currently in the 'outside' room.
player = Player("Slender", room['outside'])

while True:
    valid_directions = ["n", "e", "w", "s"]
    user_input = input("Enter cardinal direction e.g n, w, e, s \n =>")

    if user_input.lower() in valid_directions:
        player.move(user_input)
    elif user_input.lower() == "q":
        print("You quit :) bye...")
        exit()
    else:
        user_input = input(
            "Invalid direction Enter cardinal direction e.g n, w, e, s\n =>")
