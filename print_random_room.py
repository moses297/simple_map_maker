import map_make_utils
import pygame
from pygame.locals import QUIT

textures = {
    'FLOOR': pygame.image.load("./artifacts/FloorTile1.png"),
    'STONE': pygame.image.load("./artifacts/Stone1.png")
}

roomGenerator = map_make_utils.RoomGenerator(10, 10)

room = roomGenerator.randomize_room_objects()

pygame.init()
display = pygame.display.set_mode((10 * 32, 10 * 32))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit(1)

    for row in range(10):
        for col in range(10):
            display.blit(textures[room[row][col]], (row*32, col*32))
    pygame.display.update()