import pygame
import math
from game import Game

pygame.init()

# load the window of the game
pygame.display.set_caption("Kill the Death Eaters")  # title of the game
screen = pygame.display.set_mode((1080, 720))  # size of the window (largeur x hauteur)

# load the background of the game
background = pygame.image.load('assets/bg.jpg')

# import the banner
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# import button start
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# load the game
game = Game()

running = True

# loop until running is true the window will be opened
while running:
    # attribute the background to the screen
    screen.blit(background, (0, -200))
    # check if the game has started
    if game.is_playing:
        game.update(screen)
    # check if the game didn't started
    else:
        # add my button and my banner
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)
    # update the window
    pygame.display.flip()

    # check if the player close the window
    for event in pygame.event.get():
        # check if event is closed window
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("the game has been closed")
        # detect if a player leave a keyboard key
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detect if the space key is pressed
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            # check which key has been used
            # if event.key == pygame.K_RIGHT:
            #     game.player.move_right()
            # elif event.key == pygame.K_LEFT:
            #     game.player.move_left()

        # check if we pressed the mouse
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # check if we pressed the mouse on the button start
            if play_button_rect.collidepoint(event.pos):
                game.start()
