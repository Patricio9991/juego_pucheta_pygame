import pygame
from  pygame.locals import *
import pygame.time

import sys

from settings  import *
from packages.screen_functions import punto_en_rectangulo,draw_text
from gameplay_functions import main_gameplay_screen



pygame.init()

SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Battle Fantasy')



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




    SCREEN.fill(WHITE)
    play_btn = draw_text(SCREEN,"Play",FONT,BLACK,SCREEN_CENTER)


    pygame.display.flip()




pygame.quit()




    
