import pygame
from packages.screen_functions import cargar_imagenes
#fps
FPS = 10

#imagenes
PANEL_TOP = 150

WIDTH = 800
HEIGHT = 450 + PANEL_TOP #600
SCREEN_SIZE = (WIDTH,HEIGHT)
SCREEN_CENTER = (WIDTH//2,HEIGHT//2)
SCREEN_CENTER_TOP = (WIDTH //2, 100)

BG_SIZE_W_PANELS = (WIDTH,HEIGHT-PANEL_TOP)

PANELES = (0,HEIGHT-PANEL_TOP)

ALTURA_BARRA_HP_MAP = 10
ALTURA_BARRA_HP_BATTLE = 520



#font
pygame.font.init()
FONT_SIZE = 20
FONT = pygame.font.SysFont("Times New Roman",FONT_SIZE)


#colors
RED = (255,0,0)
GREEN = (0,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
GOLD = (212,175,55)



#tamaño personaje
MAP_CHARACTER_SIZE = (50,50)


#volumen sonido
MUSIC_VOLUME = 0.08


#flags menu
go_to_map = False
map = True
play = True


SPECIAL_ITEM_SIZE = (30,30)
SPECIAL_THUNDER_SIZE = (200,200)
ALTURA_SPECIAL_AVAILABLE = (600,20)


