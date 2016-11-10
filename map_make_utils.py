# Test comment
class RoomData(object):
    items = ["Book", "Sword", "Fireplace", "Door"]
    floor = ["Stone", "Poo", "Pee", "Blood"]
    #Needs more poop


class RoomGenerator(object):
    def __init__(self, room_width, room_height):
        self.room_width = room_width
        self.room_height = room_height
        self.room_type = None
        self.room_board = [self.room_width][self.room_height]

    def create_room_(self):
        pass

    def randomize_room_objects(self):
        for obj in RoomData.items:
            print (obj)