# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None
        self.items = []

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

    def display_room_details(self):
        output = "----Room Details----\n"
        output += f"Room name: {self.current_room.name}\n"
        output += f"Description: {self.current_room.description}\n"
        print(output)
