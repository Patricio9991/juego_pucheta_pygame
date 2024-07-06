import pygame
from packages.character_functions import *
from packages.screen_functions import *


#Listas con animaciones

pygame.display.set_mode((WIDTH,HEIGHT))

animaciones_skeleton = cargar_imagenes("skeleton")
animaciones_knight = cargar_imagenes("knight")
animaciones_ojo = cargar_imagenes("eye")



#personaje principal
el_cebolla = new_personaje(120,300,"knight",100,100,300,1,True,animaciones_knight)



#enemigos
el_huesos1 = new_personaje(500,370,"skeleton",10,10,10,0,True,animaciones_skeleton)
el_huesos2 = new_personaje(640,370,"skeleton",10,10,10,0,True,animaciones_skeleton)

ojo_volador = new_personaje(550, 250,"eye", 15,15,4,0,True,animaciones_ojo)


enemies = [[el_huesos1,el_huesos2],[ojo_volador]]

