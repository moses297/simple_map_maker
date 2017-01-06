import random


class RandomizeAxis(object):
    @staticmethod
    def randomize_spot_on_board(x, y):
        return random.randrange(x), random.randrange(y)

    @staticmethod
    def randomize_spot_between_range(x1, x2, y1, y2):
        return random.randrange(x1, x2), random.randrange(y1, y2)

