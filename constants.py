import pygame

pygame.init()

# Розміри екрана
WIDTH = 1536
HEIGHT = 872
HEIGHT_MAP = 792
DIFFERENCE = HEIGHT - HEIGHT_MAP

# Розмір одного квадратика матриці
CELL_SIZE = 24

# об'єкти карти
brick = 1
heart = 9
free_cell = 0

# Кількість смертей
count_death_yellow = 0
count_death_green = 0

# Розміри матриціі
MATRIX_WIDTH = WIDTH // CELL_SIZE
MATRIX_HEIGHT = HEIGHT_MAP // CELL_SIZE

# Колір фону
CELL_COLOR = (50, 105, 0)

# Головний екран
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Текст до гри
font = pygame.font.Font("Font/Montserrat-BoldItalic.ttf", 30)

text_game = font.render("Зробіть вибір:", True, "black")

text_green_win = font.render("ПЕРЕМІГ ЗЕЛЕНИЙ!!!", True, (68, 7, 92))
text_yellow_win = font.render("ПЕРЕМІГ ЖОВТИЙ!!!", True, (68, 7, 92))
text_noonewins = font.render("НІЧИЯ!!!", True, (68, 7, 92))
text_game_restart = font.render("Грати ще раз", True, "black")
restart_rect = text_game_restart.get_rect(topleft=(640, 350))

text_snow = font.render("Сніг", True, "black")
snow_text_rect = text_snow.get_rect(topleft=(640, 350))

text_pisok = font.render("Пустеля", True, "black")
pisok_text_rect = text_snow.get_rect(topleft=(640, 450))

text_grass = font.render("Джунглі", True, "black")
grass_text_rect = text_snow.get_rect(topleft=(640, 550))

# Музика
pygame.mixer.music.load('music/intro.mp3')
shoot = pygame.mixer.Sound("music/shoot.wav")
death = pygame.mixer.Sound("music/death.wav")
