import pygame
from util import PhotoRotate


class Tank:

    def __init__(self, name, hp, tank_image, control_keys, tank_coordinates):
        self.name = name
        self.hp = hp
        self.tank_image = pygame.image.load(tank_image)
        self.control_keys = control_keys
        self.tank_coordinates = tank_coordinates
        self.tank_rotate = PhotoRotate(self.tank_image)
        self.tank_image = self.tank_rotate.rotate_up

    @property
    def get_tank_icon(self):
        return self.tank_image
