import random
from utils.room_data import FloorArtifacts
from utils.pattern_generator import PatternGenerator


class Room(object):
    def __init__(self, width, height, door_locations):
        self.width = width
        self.height = height
        self.door_locations = door_locations
        self.type = None
        self.background = [[FloorArtifacts.TILES for x in range(self.width)] for y in range(self.height)]
        self.board = [['' for x in range(self.width)] for y in range(self.height)]


class RoomGenerator(object):
    def __init__(self, width, height, door_locations=None):
        assert width > 4, height > 4
        self._room = Room(width, height, door_locations)

    @property
    def room(self):
        return self._room

    def randomize_room_objects(self):
        random_floor_pattern = random.randint(1, FloorArtifacts.NUM_OF_ARTIFACTS - 1)
        pattern_generator = PatternGenerator(self._room.width, self._room.height)
        pattern = random.choice(pattern_generator.patterns)()
        for xy in pattern:
            self._room.board[xy[0]][xy[1]] = random_floor_pattern
