from room import Room
from player import Player
import textwrap

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


def move_to_room_toward(player, direction):
    if getattr(player.current_room, direction) is not None:
        player.current_room = getattr(player.current_room, direction)
    else:
        print("You can't move that way")


def display_current_player_room(player):
    # Prints the current room name
    print(player.current_room.name)

    # Prints the current description.
    print(textwrap.wrap(player.current_room.description))


while True:
    display_current_player_room(player)

    user_input = input("Enter cardinal direction e.g n, w, e, s \n =>")

    if user_input.lower() == "n":
        move_to_room_toward(player, "n_to")
    elif user_input.lower() == "s":
        move_to_room_toward(player, "s_to")
    elif user_input.lower() == "w":
        move_to_room_toward(player, "w_to")
    elif user_input.lower() == "e":
        move_to_room_toward(player, "e_to")
    elif user_input.lower() == "q":
        print("You quit :) bye...")
        break
    else:
        user_input = input(
            "Invalid letter Enter cardinal direction e.g n, w, e, s\n =>")
