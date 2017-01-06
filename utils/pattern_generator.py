import random
from randomize_tools import RandomizeAxis


class PatternGenerator(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.patterns = [self.generate_rectangle, self.generate_3x3_square]

    def generate_rectangle(self):
        pattern = []
        upper_left = RandomizeAxis.randomize_spot_on_board(self.width / 2, self.height / 2)
        down_right = RandomizeAxis.randomize_spot_between_range(upper_left[0] + 2, self.width, upper_left[1] + 2, self.height)
        for x in xrange(upper_left[0], down_right[0] + 1):
            for y in xrange(upper_left[1], down_right[1] + 1):
                if x == upper_left[0] or x == down_right[0] or y == down_right[1] or y == upper_left[1]:
                    pattern.append((y, x))
        return pattern

    def generate_3x3_square(self, starting_point=None, with_hole=None):
        if not with_hole:
            with_hole = random.choice([True, False])
        pattern = []
        if not starting_point:
            starting_point = RandomizeAxis.randomize_spot_on_board(self.width - 3, self.height - 3)
        for x in xrange(starting_point[0] + 1, starting_point[0] + 4):
            for y in xrange(starting_point[1] + 1, starting_point[1] + 4):
                if with_hole and x == starting_point[0] + 2 and y == starting_point[1] + 2:
                    continue
                pattern.append((x, y))
        return pattern
