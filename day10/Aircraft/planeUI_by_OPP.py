"""
    Game aircraft
"""
import pygame
from pygame.locals import *


def main():
    # create the game window
    window = pygame.display.set_mode((480, 700), depth=32)

    # create an instance of background image
    background = pygame.image.load("./files/background.png")

    # set a title for the display window
    pygame.display.set_caption("Aircraft")

    # set BGM
    pygame.mixer.init()
    pygame.mixer.music.load("./files/bgm.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)  # music loop, -1 means playing infinite loop

    # create an instance of player's plane
    player = pygame.image.load("./files/me2.png")

    # initial the player's plane position
    x, y = 0, 0

    while True:  # keeping display window open.
        # show the background image
        window.blit(background, (0, 0))

        # show player's plane image
        window.blit(player, (x, y))

        # get the keyboard events
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == QUIT:
                print("Quit Game.")
                exit()
                pass
            elif event.type == KEYDOWN:
                if event.type == K_a or event.key == K_LEFT:
                    print("left")
                    if x > 0:
                        x -= 5
                        pass
                elif event.type == K_d or event.key == K_RIGHT:
                    print("right")
                    if x < 310:
                        x += 5
                        pass
                    pass
                elif event.key == K_SPACE:
                    print("k_space")
                    pass

        # display content update
        pygame.display.update()
    pass


if __name__ == "__main__":
    # call main() function
    main()
