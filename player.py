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

    def launch_projectile(self):
        projectile = Projectile(self)
        self.all_projectiles.add(projectile)

    def move_right(self):
        # if the player isn't in collision with a monster
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

