import pygame
from game import Game
pygame.init()


# load the window of the game
pygame.display.set_caption("Kill the Death Eaters")  # title of the game
screen = pygame.display.set_mode((1080, 720))  # size of the window (largeur x hauteur)

# load the background of the game
background = pygame.image.load('assets/bg.jpg')

# load the game
game = Game()

running = True

# loop until running is true the window will be opened
while running:
    # attribute the background to the screen
    screen.blit(background, (0, -200))

    # attribute the image to my player
    screen.blit(game.player.image, game.player.rect)

    # actualise the health bar of the player
    game.player.update_health_bar(screen)

    # collect the projectiles of the player
    for projectile in game.player.all_projectiles:
        projectile.move()

    # collect the monsters in the game and make them move
    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)

    # attribute the image to the group of the projectiles
    game.player.all_projectiles.draw(screen)

    # attribute the image to the group of the monsters
    game.all_monsters.draw(screen)

    # check if the player wants to go right or left
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

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