import pygame
import map
import bullet
import tank
import constants
from util import ControlKeys, TankCoordinates
import time
import random
import subprocess


pygame.init()

start_time = time.time()
interval = 40
clock = pygame.time.Clock()
key = pygame.key

battlefield = map.Jungle()
control_keys1 = ControlKeys(key.key_code("w"),
                            key.key_code("s"),
                            key.key_code("d"),
                            key.key_code("a"),
                            key.key_code("SPACE"))

tank1 = tank.Tank(2, 10, "icons/tank1.png", control_keys1, TankCoordinates(2, 2))

control_keys2 = ControlKeys(key.key_code("UP"),
                            key.key_code("DOWN"),
                            key.key_code("RIGHT"),
                            key.key_code("LEFT"),
                            key.key_code("ENTER"))
tank2 = tank.Tank(5, 10, "icons/tank2.png", control_keys2, TankCoordinates(60, 29))

list_obj = []
list_obj2 = []

pygame.mixer.music.play()


def draw_circle(list_of_obj, destoy_tank):
    for elm in list_of_obj:
        if elm.bullets is not None:
            elm.draw_bullet(destoy_tank)
        else:
            list_of_obj.remove(elm)


def write_to_file(yellow_t, green_t):
    with open("D:/kursuva/info.txt", "w") as file:
        file.write(str(yellow_t) + "\n")
        file.write(str(green_t) + "\n")


keys = pygame.key.get_pressed()

gameplay = False
running = True
while running:
    constants.screen.blit(battlefield.background, (0, 90))
    if gameplay:
        if tank1.hp <= 0 or tank2.hp <= 0:
            if tank1.hp <= 0 and tank2.hp <= 0:
                constants.count_death_yellow += 1
                constants.count_death_green += 1
            elif tank1.hp <= 0:
                constants.count_death_yellow += 1
            elif tank2.hp <= 0:
                constants.count_death_green += 1

            constants.death.play()
            gameplay = False

        current_time = time.time()
        if current_time - start_time >= interval:
            bol = True
            while bol:
                random_row = random.randint(1, 62)
                random_cl = random.randint(1, 31)
                bol = battlefield.set_position_for_hp(random_cl, random_row)

            start_time = current_time

        draw_circle(list_obj, tank2)
        draw_circle(list_obj2, tank1)

        battlefield.draw_map(tank1, tank2, list_obj, list_obj2)
        battlefield.move_tank(tank1)
        battlefield.move_tank(tank2)
    else:
        constants.screen.fill((87, 88, 89))

        if tank1.hp == 0 and tank2.hp == 0:
            constants.screen.blit(constants.text_noonewins, (650, 100))
        elif tank2.hp <= 0:
            constants.screen.blit(constants.text_yellow_win, (600, 100))
        elif tank1.hp <= 0:
            constants.screen.blit(constants.text_green_win, (600, 100))

        constants.screen.blit(constants.text_game, (640, 250))
        constants.screen.blit(constants.text_snow, constants.snow_text_rect)
        constants.screen.blit(constants.text_pisok, constants.pisok_text_rect)
        constants.screen.blit(constants.text_grass, constants.grass_text_rect)

        mouse = pygame.mouse.get_pos()

        if constants.snow_text_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            battlefield = map.Snow()
            gameplay = True
        elif constants.grass_text_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            battlefield = map.Jungle()
            gameplay = True
        elif constants.pisok_text_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            battlefield = map.Pisok()
            gameplay = True
        pygame.mixer.music.play()

        if gameplay:
            battlefield.map[tank1.tank_coordinates.y][tank1.tank_coordinates.x] = 0
            tank1.tank_coordinates = TankCoordinates(2, 2)
            tank1.hp = 10
            tank1.name = 2
            battlefield.set_position(tank1)
            list_obj.clear()

            battlefield.map[tank2.tank_coordinates.y][tank2.tank_coordinates.x] = 0
            tank2.tank_coordinates = TankCoordinates(61, 30)
            tank2.hp = 10
            tank2.name = 5
            battlefield.set_position(tank2)
            list_obj2.clear()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            write_to_file(constants.count_death_yellow, constants.count_death_green)
            # Шлях до виконуваного файлу .exe
            exe_path = 'D:/projects visual/kursuvarob/x64/Debug/kursuvarob.exe'

            # Запуск виконуваного файлу
            running = False
            pygame.quit()
            subprocess.call(exe_path)

        if event.type == pygame.KEYUP and (event.key == pygame.K_SPACE or event.key == pygame.K_KP_ENTER):
            if event.key == pygame.K_SPACE:
                bullet1 = bullet.Bullet(tank1)
                list_obj.append(bullet1)
                constants.shoot.play()
            else:
                bullet2 = bullet.Bullet(tank2)
                list_obj2.append(bullet2)
                constants.shoot.play()

    pygame.display.update()
    clock.tick(10)
