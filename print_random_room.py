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


def rotate_wall(wall_tile, col, row, height, width):
    if col == height:
        wall_tile = pygame.transform.rotate(wall_tile, 180)
    if row == 0:
        wall_tile = pygame.transform.rotate(wall_tile, 90)
    if row == width:
        wall_tile = pygame.transform.rotate(wall_tile, 270)
    return wall_tile


def rotate_corner(corner_tile, col, row, height, width):
    if col == 0 and row == width:
        corner_tile = pygame.transform.rotate(corner_tile, 90)
    if col == height and row == 0:
        corner_tile = pygame.transform.rotate(corner_tile, 270)
    if col == height and row == width:
        corner_tile = pygame.transform.rotate(corner_tile, 180)
    return corner_tile


def draw_wall_area(pygame_display, door_locations):
    for col in range(HEIGHT_WITH_WALL):
        for row in range(WIDTH_WITH_WALL):
            wall_tile = pygame.image.load("./artifacts/WallTile1.png")
            corner_tile = pygame.image.load("./artifacts/CornerTile1.png")
            corner_tile = rotate_corner(corner_tile, col, row, HEIGHT_WITH_WALL - 1, WIDTH_WITH_WALL - 1)
            wall_tile = rotate_wall(wall_tile, col, row, HEIGHT_WITH_WALL - 1, WIDTH_WITH_WALL - 1)
            if in_limits(col, 0, HEIGHT_WITH_WALL - 1) and in_limits(row, 0, WIDTH_WITH_WALL - 1):
                pygame_display.blit(corner_tile, ((row) * 32, (col) * 32))
            elif in_limits(col, 0, HEIGHT_WITH_WALL - 1) or in_limits(row, 0, WIDTH_WITH_WALL - 1):
                pygame_display.blit(wall_tile, ((row) * 32, (col) * 32))


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