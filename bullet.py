import pygame
import constants
from util import PhotoRotate


class Bullet:

    def __init__(self, tank):
        self.bullet = pygame.image.load("icons/small.png")

        self.coordinate_x = tank.tank_coordinates.x * constants.CELL_SIZE
        self.coordinate_y = tank.tank_coordinates.y * constants.CELL_SIZE
        self.bullets = None

        self.position_tank = tank.tank_image
        self.tank = tank

        self.rotate = PhotoRotate(self.bullet)
        self.check()

    def add_to_bul(self, x, y):
        self.bullets = self.bullet.get_rect(topleft=(x, y))

    def check(self):
        if self.position_tank == self.tank.tank_rotate.rotate_right:
            self.add_to_bul(self.coordinate_x + 20, self.coordinate_y + constants.DIFFERENCE)
        elif self.position_tank == self.tank.tank_rotate.rotate_left:
            self.add_to_bul(self.coordinate_x - 20, self.coordinate_y + constants.DIFFERENCE)
        elif self.position_tank == self.tank.tank_rotate.rotate_up:
            self.add_to_bul(self.coordinate_x, self.coordinate_y - 20 + constants.DIFFERENCE)
        elif self.position_tank == self.tank.tank_rotate.rotate_down:
            self.add_to_bul(self.coordinate_x, self.coordinate_y + 20 + constants.DIFFERENCE)

    def draw_bullet(self, tank_destroy):
        if self.bullets:
            if self.position_tank == self.tank.tank_rotate.rotate_up:
                constants.screen.blit(self.rotate.rotate_up, (self.bullets.x, self.bullets.y))
                self.bullets.y -= constants.CELL_SIZE
                self.coordinate_y -= constants.CELL_SIZE
            elif self.position_tank == self.tank.tank_rotate.rotate_down:
                constants.screen.blit(self.rotate.rotate_down, (self.bullets.x, self.bullets.y))
                self.bullets.y += constants.CELL_SIZE
                self.coordinate_y += constants.CELL_SIZE
            elif self.position_tank == self.tank.tank_rotate.rotate_right:
                constants.screen.blit(self.rotate.rotate_right, (self.bullets.x, self.bullets.y))
                self.bullets.x += constants.CELL_SIZE
                self.coordinate_x += constants.CELL_SIZE
            elif self.position_tank == self.tank.tank_rotate.rotate_left:
                constants.screen.blit(self.rotate.rotate_left, (self.bullets.x, self.bullets.y))
                self.bullets.x -= constants.CELL_SIZE
                self.coordinate_x -= constants.CELL_SIZE
            if self.bullets.colliderect(
                    tank_destroy.get_tank_icon.get_rect(
                        topleft=(tank_destroy.tank_coordinates.x * constants.CELL_SIZE,
                                 tank_destroy.tank_coordinates.y * constants.CELL_SIZE + constants.DIFFERENCE))):
                touch = pygame.mixer.Sound("music/touchtank.wav")
                tank_destroy.hp -= 1
                touch.play()
                self.bullets = None

            if tank_destroy.hp == 0:
                tank_destroy.name = 0

            if self.coordinate_x > constants.WIDTH or self.coordinate_x < 0:
                self.bullets = None
            if self.coordinate_y > constants.HEIGHT or self.coordinate_y < 20:
                self.bullets = None

    def get_icon(self):
        return self.bullet
