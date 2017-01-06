import map_make_utils
import random
import pygame
from pygame.locals import QUIT
from utils.graphics import FloorGraphics

WIDTH = 10
HEIGHT = 10

room_generator = map_make_utils.RoomGenerator(WIDTH, HEIGHT)
for i in range(random.randint(1, 7)):
    room_generator.randomize_room_objects()
room = room_generator.room

pygame.init()
display = pygame.display.set_mode((WIDTH * 32, HEIGHT * 32))


def draw_board_to_screen(pygame_display, board):
    for col in range(HEIGHT):
        for row in range(WIDTH):
            if board[col][row]:
                pygame_display.blit(FloorGraphics.textures[board[col][row]], (row * 32, col * 32))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit(1)

    draw_board_to_screen(display, room.background)
    draw_board_to_screen(display, room.board)

    pygame.display.update()