import map_make_utils
import random
import pygame
from pygame.locals import QUIT
from utils.graphics import FloorGraphics

WIDTH = 10
HEIGHT = 10
WIDTH_WITH_WALL = WIDTH + 2
HEIGHT_WITH_WALL = HEIGHT + 2

room_generator = map_make_utils.RoomGenerator(WIDTH, HEIGHT)
for i in range(random.randint(1, 7)):
    room_generator.randomize_room_objects()
room = room_generator.room

pygame.init()
display = pygame.display.set_mode(((WIDTH + 2) * 32, (HEIGHT + 2) * 32))


def in_limits(location, min, max):
    return location == min or location == max


def draw_wall_area(pygame_display, door_locations):
    for col in range(HEIGHT_WITH_WALL):
        for row in range(WIDTH_WITH_WALL):
            if in_limits(col, 0, HEIGHT_WITH_WALL - 1) and in_limits(row, 0, WIDTH_WITH_WALL - 1):
                pygame_display.blit(pygame.image.load("./artifacts/CornerTile1.png"), ((row) * 32, (col) * 32))
            elif in_limits(col, 0, HEIGHT_WITH_WALL - 1) or in_limits(row, 0, WIDTH_WITH_WALL - 1):
                pygame_display.blit(pygame.image.load("./artifacts/WallTile1.png"), ((row) * 32, (col) * 32))


def draw_board_to_screen(pygame_display, board):
    for col in range(HEIGHT):
        for row in range(WIDTH):
            if board[col][row]:
                pygame_display.blit(FloorGraphics.textures[board[col][row]], ((row + 1) * 32, (col + 1) * 32))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit(1)

    draw_wall_area(display, "")
    draw_board_to_screen(display, room.background)
    draw_board_to_screen(display, room.board)

    pygame.display.update()