import pygame
from player import Player
from monster import Monster


# create a class game
class Game:
    def __init__(self):
        # define if the game began or not
        self.is_playing = False
        # load the player
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # define a group of monster
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        # reset the game (take out the monster and put 100 life to the player)
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
        # attribute the image to my player
        screen.blit(self.player.image, self.player.rect)

        # actualise the health bar of the player
        self.player.update_health_bar(screen)

        # collect the projectiles of the player
        for projectile in self.player.all_projectiles:
            projectile.move()

        # collect the monsters in the game and make them move
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # attribute the image to the group of the projectiles
        self.player.all_projectiles.draw(screen)

        # attribute the image to the group of the monsters
        self.all_monsters.draw(screen)

        # check if the player wants to go right or left
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)
