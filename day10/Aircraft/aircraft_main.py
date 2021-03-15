"""
    Aircraft Game by OPP
"""

import pygame
import random
import time
from pygame.locals import *

"""
    an instance of the player plane by OOP
        1. show instance in the window
        2. moving the plane instance in the window
"""


# A PlayerPlane Class
class PlayerPlane(object):
    def __init__(self, window):
        """
        initial constructor
        :param window:  # the instance of main window
        """
        # the plane's default position (the instance)
        self.x = 180
        self.y = 600
        # set the main windows
        self.window = window
        # load the plane image
        self.image = pygame.image.load("./files/me2.png")

        # a list for storage of bullets
        self.bullet_list = []
        pass

    def move_left(self):
        """
        move to left
        :return:
        """
        if self.x > 0:
            self.x -= 10
        pass

    def move_right(self):
        """
        move to right
        :return:
        """
        if self.x < 350 - 40:
            self.x += 10
        pass

    def show_plane(self):
        """
        show the player plane in the main window
        :return:
        """
        self.window.blit(self.image, (self.x, self.y))

        # optimizing bullet logic, to avoid out of window bullets
        filter_bullet = []
        for bu_item in self.bullet_list:
            if bu_item.out_of_bound_bullet():
                filter_bullet.append(bu_item)
                pass
            pass
        for i in filter_bullet:
            self.bullet_list.remove(i)
            pass
        for bu_item2 in self.bullet_list:
            bu_item2.show_bullet()  # show bullets' position
            bu_item2.bullet_move()  # show bullets' moving

    # fire bullet
    def fire_bullet(self):
        # an object of Class Bullet
        new_bullet = Bullet(self.x, self.y, self.window)
        self.bullet_list.append(new_bullet)
        pass

    pass


"""
    A Bullet Class
"""


class Bullet(object):
    def __init__(self, x, y, window):
        """
        Initial Constructor
        :param x:
        :param y:
        :param window:
        """
        self.x = x + 14
        self.y = y - 25
        self.window = window
        self.image = pygame.image.load("./files/bullet1.png")
        pass

    def show_bullet(self):
        self.window.blit(self.image, (self.x, self.y))
        pass

    def bullet_move(self):
        self.y -= 2
        pass

    # detect out of window bullets
    def out_of_bound_bullet(self):
        """
        Determine if bullets are out of window
        :return:
        """
        if self.y < 0:
            return True
        else:
            return False
        pass


# A Enemy's Plane Class
class EnemyPlane(object):
    def __init__(self, window):
        """
        Initial Constructor
        :param window:
        """
        # enemy plane's default position
        self.x = 0
        self.y = 0
        # set a default position for enemy plane
        self.direction = "right"
        # set the main window
        self.window = window

        # a list for storing bullets
        self.bullet_list = []
        self.enemy_image = "./files/enemy2.png"
        self.image = pygame.image.load(self.enemy_image)
        pass

    pass

    def show_plane(self):
        """
        show enemy plane's position,
        and the bullets' position
        :return:
        """
        self.window.blit(self.image, (self.x, self.y))
        pass

        # optimizing bullet logic, to avoid out of window bullets
        invalid_bullet = []
        for bu_item in self.bullet_list:
            if bu_item.out_of_bound_bullet():
                invalid_bullet.append(bu_item)
                pass
            pass
        for i in invalid_bullet:
            self.bullet_list.remove(i)
            pass
        for bu_item2 in self.bullet_list:
            bu_item2.show_bullet()  # show bullets' position
            bu_item2.bullet_move()  # show bullets' moving

    # fire bullet randomly

    def fire_bullet(self):
        # an object of Class Bullet
        number = random.randint(1, 20)
        if number == 3:
            new_bullet = EnemyBullet(self.x, self.y, self.window)
            self.bullet_list.append(new_bullet)
        pass

    def plane_move(self):
        """
        A fucntion for
        Enemy Plane moving randomly
        :return:
        """
        if self.direction == "right":
            self.x += 2
            pass
        elif self.direction == "left":
            self.x -= 2
            pass
        elif self.x > 450 - 20:
            self.direction = "left"
            pass
        elif self.x < 0:
            self.direction = "right"
            pass


# The EnemyBullet Class
class EnemyBullet(object):
    def __init__(self, x, y, window):
        """
        Initial Constructor
        Enemy Bullet
        :param x:
        :param y:
        :param window:
        """
        self.x = x
        self.y = y + 5
        self.window = window
        self.image = pygame.image.load("./files/bullet2.png")
        pass

    pass

    def show_bullet(self):
        self.window.blit(self.image, (self.x, self.y))
        pass

    def bullet_move(self):
        self.y += 2
        pass

    def out_of_bound_bullet(self):
        """
        Determine out of bound bullets
        :return:
        """
        if self.y > 700:
            return True
        else:
            return False
        pass


# keyboard detection function
def key_control(plane_obj):
    """
    A function for detection of Keyboard
    :param plane_obj: the object of plane for detection
    :return:
    """
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
                # call move_left() function to move plane
                plane_obj.move_left()
                pass
            elif event.type == K_d or event.key == K_RIGHT:
                print("right")
                # call move_right() function to move plane
                plane_obj.move_right()
                pass
            elif event.key == K_SPACE:
                print("k_space")
                plane_obj.fire_bullet()
                pass
            pass


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
    player = PlayerPlane(window)

    # create an instance of enemy plane
    enemy = EnemyPlane(window)

    # initial the player's plane position
    x, y = 0, 0

    while True:  # keeping display window open.
        # show the background image
        window.blit(background, (0, 0))

        # show player's plane image
        player.show_plane()

        # show enemy's plane image
        enemy.show_plane()
        enemy.plane_move()  # enemy plane moving
        enemy.fire_bullet()  # enemy plane firing

        # call key_control function
        key_control(player)

        # display content update
        pygame.display.update()
        # time.sleep(1)
        pygame.time.Clock().tick(10)
    pass


if __name__ == "__main__":
    # call main() function
    main()
