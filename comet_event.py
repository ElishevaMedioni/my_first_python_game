import pygame
from comet import Comet

# create a class to handle the event comet
class CometFallEvent:
    # create a counter during the chargement
    def __init__(self):
        self.percent = 0
        self.percent_speed = 33
        # define a group of sprite to store the comets
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed/100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        # appear the first comet
        self.all_comets.add(Comet())

    def attempt_fall(self):
        if self.is_full_loaded():
            print("Pluie de comet")
            self.meteor_fall()
            self.reset_percent()

    def update_bar(self, surface):
        # add percentage to the bar
        self.add_percent()

        # rain of comet
        self.attempt_fall()

        # black bar (background)
        pygame.draw.rect(surface, (0, 0, 0), [
            0,  # x axis
            surface.get_height() - 20,  # y axis
            surface.get_width(),  # window height
            10  # width of the bar
        ])
        # red bar (event bar)
        pygame.draw.rect(surface, (187, 11, 11), [
            0,  # x axis
            surface.get_height() - 20,  # y axis
            (surface.get_width() / 100) * self.percent,  # window height
            10  # width of the bar
        ])
