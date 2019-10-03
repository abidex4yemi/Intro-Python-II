# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def display_all_item(self):
        output = "----All items:----\n"
        if len(self.current_room.items) == 0:
            output += "No items available"
        else:
            for item in self.current_room.items:
                output += f"* {item.name} {item.description}\n"
        output += "--------------\n"

        return output

    def add_item(self, items):
        for item in items:
            self.items.append(item)

        return self.items

    def get_item(self, item_name):
        new_item = []
        output = ""

        for item in self.items:
            if item.name == item_name:
                output = item_name
            else:
                new_item.append(item)
        self.items = new_item
        return output

    def display_player_room_details(self):
        output = "----Player room Details----\n"
        output += f"Room name: {self.current_room.name}\n"
        output += f"Description: {self.current_room.description}\n"
        output += f"{self.display_all_item()}"
        output += "----------------------------\n"
        print(output)

    def move(self, direction):
        if getattr(self.current_room, f"{direction}_to") is not None:
            self.current_room = getattr(
                self.current_room, f"{direction}_to")
            self.display_player_room_details()
        else:
            print("You can't move that way")
