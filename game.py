import pygame
from player import Player

# create a class game
class Game:
    def __init__(self):
        # load the player
        self.player = Player()
        self.pressed = {}
