import pygame

#fps
FPS = 60

#imagenes
PANEL_TOP = 150

WIDTH = 800
HEIGHT = 450 + PANEL_TOP #600
SCREEN_SIZE = (WIDTH,HEIGHT)

BG_SIZE_W_PANELS = (WIDTH,HEIGHT-PANEL_TOP)

PANELES = (0,HEIGHT-PANEL_TOP)



#font
pygame.font.init()
FONT = pygame.font.SysFont("Times New Roman",26)


#colors
RED = (255,0,0)
GREEN = (0,255,0)