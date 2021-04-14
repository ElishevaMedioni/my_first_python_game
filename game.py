import pygame
from player import Player
from monster import Monster

# create a class game
class Game:
    def __init__(self):
        # load the player
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # define a group of monster
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)
