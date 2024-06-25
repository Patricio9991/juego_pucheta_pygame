import pygame
from settings  import *
from packages.screen_functions import *
from packages.character_functions import *



pygame.init()

SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Battle')

clock = pygame.time.Clock()

#----load images-----
#Background

backgorunds = [pygame.image.load('./assets/bg_0.png'), pygame.image.load('./assets/bg_1.png')]

scaled_bgs = scale_image(BG_SIZE_W_PANELS,backgorunds)

#Panel

panel = pygame.image.load('./assets/panel.png')

animaciones_knight = cargar_imagenes("knight")
animaciones_skeleton = cargar_imagenes("skeleton")


el_cebolla = new_personaje(130,300,"knight",27,30,4,6,True,animaciones_knight)
el_huesos1 = new_personaje(400,370,"skeleton",10,10,10,0,True,animaciones_skeleton)
el_huesos2 = new_personaje(560,370,"skeleton",10,10,10,0,True,animaciones_skeleton)

enemies = [el_huesos1,el_huesos2]

print(el_cebolla["animation_list"])




run = True

while run:
    clock.tick(FPS)

    draw_bg_layers(SCREEN,scaled_bgs,(0,0))
    draw(SCREEN,panel,PANELES)

    write_panels(SCREEN,f"El cebolla {el_cebolla["hp"]}",FONT,GREEN,30,HEIGHT-PANEL_TOP + 40)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for enemie in enemies:
        draw(SCREEN,enemie["animation"],enemie["rect"])

    animate_character(el_huesos1,'a')

    
    draw(SCREEN,el_cebolla["animation"],el_cebolla["rect"])
    animate_character(el_cebolla,"a")




    health_bar(SCREEN,el_cebolla["hp"],el_cebolla["max_hp"])

    # health_bar(SCREEN,el_huesos1["hp"],el_huesos1["max_hp"],False)



    pygame.display.flip()
    



pygame.quit()