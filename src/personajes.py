import pygame
from packages.character_functions import *
from packages.screen_functions import *


#Listas con animaciones

pygame.display.set_mode((WIDTH,HEIGHT))

animaciones_skeleton = cargar_imagenes("skeleton")
animaciones_knight = cargar_imagenes("knight")
animaciones_ojo = cargar_imagenes("eye")
animaciones_boss = cargar_imagenes("final_boss")




#personaje principal
el_cebolla = new_personaje(120,300,"knight",100,100,5,1,True,animaciones_knight)



#enemigos
el_huesos1 = new_personaje(500,370,"Skeleton",10,10,10,0,True,animaciones_skeleton)
el_huesos2 = new_personaje(640,370,"Skeleton",10,10,10,0,True,animaciones_skeleton)
el_huesos3 = new_personaje(500,370,"Skeleton",10,10,10,0,True,animaciones_skeleton)
el_huesos4 = new_personaje(640,370,"Skeleton",10,10,10,0,True,animaciones_skeleton)

ojo_volador = new_personaje(550, 250,"Eye", 15,15,4,0,True,animaciones_ojo)


final_boss = new_personaje(640,300,"Death",60,60,10,0,True,animaciones_boss)


enemies = [[el_huesos1,el_huesos2],[el_huesos3,el_huesos4],[ojo_volador],[final_boss]]





