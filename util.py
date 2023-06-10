import pygame


class ControlKeys:
    def __init__(self, UP, DOWN, RIGHT, LEFT, FIRE):
        self.DOWN = DOWN
        self.UP = UP
        self.RIGHT = RIGHT
        self.LEFT = LEFT
        self.FIRE = FIRE


class PhotoRotate:
    def __init__(self, image):
        self.rotate_left = pygame.transform.rotate(image, 90)
        self.rotate_down = pygame.transform.rotate(self.rotate_left, 90)
        self.rotate_right = pygame.transform.rotate(self.rotate_down, 90)
        self.rotate_up = pygame.transform.rotate(self.rotate_right, 90)


class TankCoordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y
