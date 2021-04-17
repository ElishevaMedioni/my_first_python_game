import pygame
import random

class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = random.randint(1, 3)

    def damage(self, amount):
        # inflict damage to the monster
        self.health -= amount

        # check if the health is zero
        if self.health <=0:
            # reappear like a new monster
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 3)
            self.health = self.max_health

    def update_health_bar(self, surface):
        # define a color for the health bar
        bar_color = (111, 210, 46) # color with the code RGB

        # define a color for the background of the health bar
        back_bar_color = (60, 63, 60)

        # define the position of the health bar and it width and thickness
        bar_position = [self.rect.x + 10, self.rect.y - 20, self.health, 5]

        # define the position of the background of the health bar
        back_bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]

        # draw the health bar
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def forward(self):
        # the move is possible only if there aren't collision with a player
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # if the monster is in collision with the player
        else:
            # inflict damage to the player
            self.game.player.damage(self.attack)

