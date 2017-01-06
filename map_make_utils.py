import random


def room_print(room):
    for i in room:
        print i


class RandomizeAxis(object):
    @staticmethod
    def randomize_spot_on_board(x, y):
        return random.randrange(x), random.randrange(y)

    @staticmethod
    def randomize_spot_between_range(x1, x2, y1, y2):
        return random.randrange(x1, x2), random.randrange(y1, y2)


class PatternGenerator(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.patterns = [self.generate_rectangle]

    def generate_rectangle(self):
        pattern = []
        upper_left = RandomizeAxis.randomize_spot_on_board(self.width / 2, self.height / 2)
        down_right = RandomizeAxis.randomize_spot_between_range(upper_left[0] + 2, self.width, upper_left[1] + 2, self.height)
        for x in xrange(upper_left[0], down_right[0] + 1):
            for y in xrange(upper_left[1], down_right[1] + 1):
                if x == upper_left[0] or x == down_right[0] or y == down_right[1] or y == upper_left[1]:
                        pattern.append((x, y))
        return pattern

    def generate_3x3_square(self, starting_point=None):
        pattern = []
        if not starting_point:
            RandomizeAxis.randomize_spot_on_board(self.width - 2, self.height - 2)
        for x in xrange(starting_point[0] + 1):
            for y in xrange(starting_point[1] + 1):
                pattern.append((x, y))
        return pattern


class RoomData(object):
    items = ["Book", "Sword", "Fireplace", "Door"]
    floor = ["Stone", "Poo", "Pee", "Blood"]


class Room(object):
    def __init__(self, width, height, door_locations):
        self.width = width
        self.height = height
        self.door_locations = door_locations
        self.type = None
        self.board = [['FLOOR' for x in range(self.width)] for y in range(self.height)]


class RoomGenerator(object):
    def __init__(self, width, height, door_locations=None):
        assert width > 4, height > 4
        self.room = Room(width, height, door_locations)

    def create_room_(self):
        pass

    def randomize_room_objects(self):
        a = random.choice(RoomData.floor)
        g = PatternGenerator(self.room.width, self.room.height)
        pat = g.patterns[0]()
        for xy in pat:
            self.room.board[xy[0]][xy[1]] = 'STONE'
        room_print(self.room.board)
        return self.room.board