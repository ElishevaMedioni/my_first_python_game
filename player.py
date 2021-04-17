import pygame
from projectile import Projectile


# create a class player
class Player(pygame.sprite.Sprite):  # the class herite form the class sprite
    # (classe pour les objets graphique qui se deplacent)

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5  # vitesse de deplacement du joueur
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount

    def launch_projectile(self):
        projectile = Projectile(self)
        self.all_projectiles.add(projectile)

    def move_right(self):
        # if the player isn't in collision with a monster
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def update_health_bar(self, surface):
        # define a color for the health bar
        bar_color = (111, 210, 46)  # color with the code RGB

        # define a color for the background of the health bar
        back_bar_color = (60, 63, 60)

        # define the position of the health bar and it width and thickness
        bar_position = [self.rect.x + 50, self.rect.y, self.health, 7]

        # define the position of the background of the health bar
        back_bar_position = [self.rect.x + 50, self.rect.y, self.max_health, 7]

        # draw the health bar
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)
