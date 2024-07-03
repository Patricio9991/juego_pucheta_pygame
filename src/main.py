import pygame
from  pygame.locals import *

from settings  import *
from packages.screen_functions import *
from packages.character_functions import *

from personajes import *
from variables_flags import *



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




#Configuracion Sonido:

# colision_sound = pygame.mixer.Sound("./src/assets/coin.mp3")
pygame.mixer.music.load("./src/assets/audio/battle_theme.mp3")

playing_music = True
flag_mute = False

pygame.mixer.music.set_volume(0.08)
pygame.mixer.music.play()

enemie_index = 0
play = True

while play:
    clock.tick(FPS)
    print(map,battle)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            play = False


    while map:

        clock.tick(FPS)


        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                map = False
                play = False
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
            if el_cebolla["map_image_rect"].right > WIDTH:
                el_cebolla["map_image_rect"].right = WIDTH
            el_cebolla["map_image_rect"].right += movement_speed
        
        if move_left and el_cebolla["map_image_rect"].left > 0:
            print(el_cebolla["map_image_rect"].left)
            if el_cebolla["map_image_rect"].left < 0:
                el_cebolla["map_image_rect"].right = 0
            el_cebolla["map_image_rect"].left -= movement_speed
            
        
        if move_down and el_cebolla["map_image_rect"].bottom < HEIGHT:
            if el_cebolla["map_image_rect"].bottom > HEIGHT:
                el_cebolla["map_image_rect"].bottom = HEIGHT
            print(el_cebolla["map_image_rect"].bottom)
            el_cebolla["map_image_rect"].bottom += movement_speed
        
        if move_up and el_cebolla["map_image_rect"].top > 0:
            print(el_cebolla["map_image_rect"].top)
            if el_cebolla["map_image_rect"].top < 0:
                el_cebolla["map_image_rect"].top = 0
            el_cebolla["map_image_rect"].top -= movement_speed


        
        if move_left:
            draw(SCREEN,pygame.transform.flip(el_cebolla["map_image"],True,False),el_cebolla["map_image_rect"])
        else:
            draw(SCREEN,el_cebolla["map_image"],el_cebolla["map_image_rect"])

        for i in range(len(enemies)):

            draw_enemie_in_map(SCREEN,el_cebolla,enemies[i])
            
            for j in range(len(enemies[i])):
                if detectar_colision(el_cebolla["map_image_rect"], enemies[i][j]["map_image_rect"]):
                        map = False
                        battle = True
                        enemie_index = i #indice del tipo de enemigo que colisiono
                        print("colision")

        if map:
            health_bar(SCREEN,el_cebolla["hp"],el_cebolla["max_hp"],ALTURA_BARRA_HP_MAP)
        

        pygame.display.flip()


    while battle:
        clock.tick(FPS)

        draw_bg_layers(SCREEN,scaled_bgs,(0,0))
        draw(SCREEN,panel,PANELES)

        attack_btn  = write_panels(SCREEN,"Attack",FONT,BLACK,(300,HEIGHT-PANEL_TOP + 20))
        potion_btn = write_panels(SCREEN,"Potion",FONT,BLACK,(300,HEIGHT-PANEL_TOP + 50))
        huir_btn = write_panels(SCREEN,"Huir",FONT,BLACK,(300,HEIGHT-PANEL_TOP + 80))
        pass_btn = write_panels(SCREEN,"Pass",FONT,BLACK,(300,HEIGHT-PANEL_TOP + 110))
        special_btn = write_panels(SCREEN,"SPECIAL",FONT,GOLD,(100,HEIGHT-PANEL_TOP + 120))




        for event in pygame.event.get():
            if evento.type == pygame.QUIT:
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
                    if punto_en_rectangulo(event.pos,huir_btn):
                        map = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    battle = False


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
            draw_text(SCREEN,f"{turn_cooldown}",FONT,(0,0,0),SCREEN_CENTER_TOP)
            animate_character(el_cebolla,'i')
            if turn_cooldown <= turn_wait_time and current_turn == 1:
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

            elif turn_cooldown >= turn_wait_time:
                draw_text(SCREEN,"FIN DEL TURNO",FONT,RED,(400,200))
                turn_cooldown = 0
                current_turn += 1

        
            if current_turn == 2 and turn_cooldown<turn_wait_time:
                turn_cooldown += 1
                animate_character(el_huesos1,'i')
                animate_character(ojo_volador,'i')
            elif turn_cooldown >= turn_wait_time:
                draw_text(SCREEN,"FIN DEL TURNO",FONT,RED,(400,200))
                turn_cooldown = 0
                current_turn += 1
            
            if current_turn == 3 and turn_cooldown<turn_wait_time:
                turn_cooldown += 1
                animate_character(el_huesos2,'i')
            elif turn_cooldown >= turn_wait_time:
                draw_text(SCREEN,"FIN DEL TURNO",FONT,RED,(400,200))
                turn_cooldown = 0
                current_turn += 1

        if current_turn > 3:
            current_turn = 1
            action_knight = False
            atk_flag = True
            potion_flag = True
            turn_cooldown = 0

                    
    
                    
        draw(SCREEN,el_cebolla["animation"],el_cebolla["rect"])
        write_panels(SCREEN,f"El cebolla {el_cebolla["hp"]}",FONT,GREEN,(100,HEIGHT-PANEL_TOP + 40))
        health_bar(SCREEN,el_cebolla["hp"],el_cebolla["max_hp"],ALTURA_BARRA_HP_BATTLE)


        for i in range(len(enemies[enemie_index])):
            altura_nombre = (i+1) *40
            altura_barra_hp = i *45
            draw(SCREEN,pygame.transform.flip(enemies[enemie_index][i]["animation"],True,False),enemies[enemie_index][i]["rect"])
            write_panels(SCREEN,f"El Huesos {enemies[enemie_index][i]["hp"]}",FONT,GREEN,(700,HEIGHT-PANEL_TOP + altura_nombre))
            health_bar(SCREEN,enemies[enemie_index][i]["hp"],enemies[enemie_index][i]["max_hp"],altura_barra_hp,False )

        pygame.draw.rect(SCREEN,WHITE,attack_btn,1)
        pygame.draw.rect(SCREEN,WHITE,potion_btn,1)
        pygame.draw.rect(SCREEN,WHITE,huir_btn,1)
        pygame.draw.rect(SCREEN,WHITE,pass_btn,1)






        pygame.display.flip()

    pygame.display.flip()


    
    
        



pygame.quit()