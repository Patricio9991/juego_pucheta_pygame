import pygame
from  pygame.locals import *

from settings  import *
from packages.screen_functions import *
from packages.character_functions import *
from packages.variables_flags import *



pygame.init()

SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Battle')

clock = pygame.time.Clock()

pygame.time.get_ticks()

#----load images-----
#Background

backgorunds = [pygame.image.load('./src/assets/bg_0.png'), pygame.image.load('./src/assets/bg_1.png')]
scaled_bgs = scale_image(BG_SIZE_W_PANELS,backgorunds)

#Panel
panel = pygame.image.load('./src/assets/panel.png')

animaciones_knight = cargar_imagenes("knight")
animaciones_skeleton = cargar_imagenes("skeleton")

print(animaciones_knight)

el_cebolla = new_personaje(120,300,"knight",13,30,3,6,True,animaciones_knight)
el_huesos1 = new_personaje(500,370,"skeleton",10,10,10,0,True,animaciones_skeleton)
el_huesos2 = new_personaje(640,370,"skeleton",10,10,10,0,True,animaciones_skeleton)

enemies = [el_huesos1,el_huesos2]

current_turn = 1
total_characters = 3
turn_cooldown = 0
turn_wait_time = 90  


is_animating_knight = False
atk_flag = True

move_right = False
speed = 3

flag_heal = True



#Configuracion Sonido:

# colision_sound = pygame.mixer.Sound("./src/assets/coin.mp3")
pygame.mixer.music.load("./src/assets/audio/battle_theme.mp3")

playing_music = True
flag_mute = False

pygame.mixer.music.set_volume(0.08)
pygame.mixer.music.play()






move_down = False
move_left = False
move_right = False
move_up = False


battle = False

map = True

while map:

    clock.tick(FPS)



    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            map = False

        if evento.type == pygame.KEYDOWN:
                print("keydown")
                if evento.key == K_SPACE:
                    map = False
                    battle = True
                if evento.key == K_LEFT:
                    print("Flecha izquieda")
                    move_left = True
                    move_right = False

                if evento.key == K_RIGHT:
                    print("Flecha derecha")
                    move_right = True
                    move_left = False

                if evento.key == K_UP:
                    print("Flecha arriba")
                    move_up = True

                if evento.key == K_DOWN:
                    print("Flecha aabajo")
                    move_down = True

        if evento.type == pygame.KEYUP:
            print("keydown")
            if evento.key == K_LEFT:
               print("Flecha izquieda")
               move_left = False

            if evento.key == K_RIGHT:
               print("Flecha derecha")
               move_right = False

            if evento.key == K_UP:
               print("Flecha arriba")
               move_up = False

            if evento.key == K_DOWN:
               print("Flecha aabajo")
               move_down = False




    SCREEN.fill((255,255,255))

    
    if move_right and el_cebolla["map_image_rect"].right < WIDTH:
        print(el_cebolla["map_image_rect"].right)
        el_cebolla["map_image_rect"].right += 10
    
    if move_left and el_cebolla["map_image_rect"].left > 0:
        print(el_cebolla["map_image_rect"].left)
        el_cebolla["map_image_rect"].left -= 10
    
    if move_down and el_cebolla["map_image_rect"].bottom < HEIGHT:
        print(el_cebolla["map_image_rect"].bottom)

        el_cebolla["map_image_rect"].bottom += 10
    
    if move_up and el_cebolla["map_image_rect"].top > 0:
        print(el_cebolla["map_image_rect"].top)

        el_cebolla["map_image_rect"].top -= 10


    

        
    draw(SCREEN,el_cebolla["map_image"],el_cebolla["map_image_rect"])
    

    pygame.display.flip()







while battle:
    clock.tick(FPS)

    draw_bg_layers(SCREEN,scaled_bgs,(0,0))
    draw(SCREEN,panel,PANELES)

    attack_btn  = write_panels(SCREEN,"Attack",FONT,(0,0,0),(300,HEIGHT-PANEL_TOP + 20))
    potion_btn = write_panels(SCREEN,"Potion",FONT,(0,0,0),(300,HEIGHT-PANEL_TOP + 60))
    pass_btn = write_panels(SCREEN,"Pass",FONT,(0,0,0),(300,HEIGHT-PANEL_TOP + 120))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            battle = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if punto_en_rectangulo(event.pos,attack_btn) and atk_flag:
                    action_knight = True
                    print(action_knight,atk_flag)
                    potion_flag = False
                if punto_en_rectangulo(event.pos,potion_btn) and potion_flag:
                    action_knight = True
                    atk_flag = False
                    print("pociones")
    

                if punto_en_rectangulo(event.pos,pass_btn):
                    current_turn += 1

        

                

    

        if event.type == pygame.KEYDOWN: 
            if event.key == K_m:
                if playing_music:
                    pygame.mixer.music.pause()
                    
                    flag_mute = True
                else:
                    pygame.mixer.music.unpause()
                    flag_mute = False
                playing_music = not playing_music
                
            if event.key == K_p:
                wait_user(K_p)






    if flag_mute:
        draw_text(SCREEN,"Mute",FONT,GREEN,(400,500)) 


    if el_cebolla["alive"]:
        draw_text(SCREEN,f"{turn_cooldown}",FONT,(0,0,0),(100,100))
        animate_character(el_cebolla,'i')
        if current_turn == 1 and turn_cooldown<turn_wait_time:
            turn_cooldown += 1
            if action_knight and atk_flag:
                animate_character(el_cebolla,'a')
                attack(el_cebolla,el_huesos1)
                print("atacar")
                action_knight = False
                turn_cooldown = 0
                current_turn += 1
            elif action_knight and potion_flag:
                if el_cebolla["potions"] > 0:
                    heal(el_cebolla)
                else:
                    draw_text(SCREEN,"NO HAY MAS POSIONES",FONT,RED,(400,200))
                turn_cooldown = 0
                current_turn += 1
         
       
        if current_turn == 2 and turn_cooldown<turn_wait_time:
            turn_cooldown += 1
            animate_character(el_huesos1,'i')
        
        if current_turn == 3 and turn_cooldown<turn_wait_time:
            turn_cooldown += 1
            animate_character(el_huesos2,'i')

    if current_turn > 3:
        current_turn = 1
        action_knight = False
        atk_flag = True
        potion_flag = True
        turn_cooldown = 0

                
 
                


                


    draw(SCREEN,el_cebolla["animation"],el_cebolla["rect"])
    write_panels(SCREEN,f"El cebolla {el_cebolla["hp"]}",FONT,GREEN,(100,HEIGHT-PANEL_TOP + 40))
    health_bar(SCREEN,el_cebolla["hp"],el_cebolla["max_hp"])


    for i in range(len(enemies)):
        altura_nombre = (i+1) *40
        altura_barra_hp = i *45
        draw(SCREEN,enemies[i]["animation"],enemies[i]["rect"])
        write_panels(SCREEN,f"El Huesos {enemies[i]["hp"]}",FONT,GREEN,(700,HEIGHT-PANEL_TOP + altura_nombre))
        health_bar(SCREEN,enemies[i]["hp"],enemies[i]["max_hp"],altura_barra_hp,False )

    pygame.draw.rect(SCREEN,WHITE,attack_btn,1)
    pygame.draw.rect(SCREEN,WHITE,potion_btn,1)
    pygame.draw.rect(SCREEN,WHITE,pass_btn,1)






    pygame.display.flip()
    



pygame.quit()