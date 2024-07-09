import pygame
from  pygame.locals import *
import pygame.time

import sys

from settings  import *
from packages.screen_functions import punto_en_rectangulo,draw_text
from packages.gameplay_functions import *



pygame.init()

SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Battle Fantasy')

backgrounds = cargar_imagenes("backgrounds")
menu_img = backgrounds[0][0]
scaled_menu_bg =  scale_image(SCREEN_SIZE,menu_img)


while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if punto_en_rectangulo(event.pos,play_btn):
                   go_to_map = True

    if go_to_map: 
        main_gameplay_screen(SCREEN,map)


    draw(SCREEN,scaled_menu_bg,(0,0))
    play_btn = draw_text(SCREEN,"Play",FONT,BLACK,SCREEN_CENTER)


    pygame.display.flip()




pygame.quit()




    
