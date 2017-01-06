from room_data import FloorArtifacts
from os.path import join
import pygame

ARTIFACTS_PATH = './artifacts/'


def load_artifact(artifact):
    return pygame.image.load(join(ARTIFACTS_PATH, artifact))


class FloorGraphics(object):
    textures = ['' for i in xrange(FloorArtifacts.NUM_OF_ARTIFACTS + 1)]
    textures[FloorArtifacts.BLOOD] = load_artifact("Blood1.png")
    textures[FloorArtifacts.PEE] = load_artifact("Pee2.png")
    textures[FloorArtifacts.POO] = load_artifact("Poo1.png")
    textures[FloorArtifacts.STONE] = load_artifact("Stone1.png")
    textures[FloorArtifacts.TILES] = load_artifact("FloorTile1.png")
