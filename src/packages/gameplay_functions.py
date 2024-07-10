import pygame
from  pygame.locals import *
import pygame.time

import sys

from settings import *
from packages.screen_functions import *
from packages.character_functions import *
from personajes import *
from special_items import *
from score import *



backgrounds = cargar_imagenes("backgrounds")
scaled_bg_map = scale_image(SCREEN_SIZE,backgrounds[1],True)



def battle_screen(battle,SCREEN,enemie = 0):
    clock = pygame.time.Clock()

    #----load images-----
    #Background
    
    scaled_bgs = scale_image(BG_SIZE_W_PANELS,backgrounds[0],True)


    #Panel
    panel = pygame.image.load('./src/assets/panel.png')

    #Variables turnos
    current_turn = 1
    turn_cooldown = 0
    turn_wait_time = 30  
    enemy_turn_wait_time = 15
    enemie_phase = 1
    enemie_index = enemie
    enemy_focused = 0
    next_battle = False

    #Actions Knight
    action_knight = False
    atk_flag = True
    potion_flag = True
    flag_heal = True
    special_flag = True

    playing_music = True
    flag_mute = False


    if battle:
        pygame.mixer.music.load("./src/assets/audio/battle_theme.mp3")
        pygame.mixer.music.set_volume(MUSIC_VOLUME)
        pygame.mixer.music.play()

    while battle:
        clock.tick(FPS)



        draw_bg_layers(SCREEN,scaled_bgs,(0,0))
        draw(SCREEN,panel,PANELES)

        attack_btn  = write_panels(SCREEN,"Attack",FONT,BLACK,(300,HEIGHT-PANEL_TOP + 20))
        potion_btn = write_panels(SCREEN,f"Potion x{el_cebolla["potions"]}",FONT,BLACK,(300,HEIGHT-PANEL_TOP + 50))
        huir_btn = write_panels(SCREEN,"Huir",FONT,BLACK,(300,HEIGHT-PANEL_TOP + 80))
        pass_btn = write_panels(SCREEN,"Pass",FONT,BLACK,(300,HEIGHT-PANEL_TOP + 110))
        special_btn = write_panels(SCREEN,f"SPECIAL x{el_cebolla["special_atk"]//5}",FONT,GOLD,(100,HEIGHT-PANEL_TOP + 120))




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
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

                        return True

                    if punto_en_rectangulo(event.pos,special_btn) and special_flag:
                        action_knight = True
                        atk_flag = False
                        potion_flag = False



            if event.type == pygame.KEYDOWN: 
                if event.key == K_m:
                    if playing_music:
                        pygame.mixer.music.pause()
                        flag_mute = True
                    else:
                        pygame.mixer.music.unpause()
                        flag_mute = False
                    playing_music = not playing_music
            


        if flag_mute:
            draw_text(SCREEN,"Mute",FONT,GREEN,(400,500)) 

        
        

        if el_cebolla["alive"]:
            draw_text(SCREEN,f"{turn_cooldown}",FONT,BLACK,SCREEN_CENTER_TOP)
            animate_character(el_cebolla,'i')

            animate_character(el_huesos1,'i')
            animate_character(el_huesos2,'i')
            animate_character(el_huesos3,'i')
            animate_character(el_huesos4,'i')
            
            animate_character(ojo_volador,'i')
            animate_character(final_boss,'i')


            if len(enemies[enemie_index]) > 0:
                target = enemies[enemie_index][0]



                if turn_cooldown <= turn_wait_time and current_turn == 1:
                    turn_cooldown += 1
                    if action_knight and atk_flag:
                        animate_character(el_cebolla,'a')
                        attack(el_cebolla,target)
                        print("atacar")
                        action_knight = False
                        turn_cooldown = 0
                        current_turn += 1

                    elif action_knight and potion_flag:
                        if el_cebolla["potions"] > 0:
                            heal(el_cebolla)
                            turn_cooldown = 0
                            current_turn += 1
                        else:
                            draw_text(SCREEN,"NO HAY MAS POSIONES",FONT,RED,(WIDTH//2,200))
                            turn_cooldown = 0
                            current_turn += 1
                            
                    elif action_knight and special_flag:
                        if el_cebolla["special_atk"] >= 5:
                            attack(el_cebolla,target,True)
                            thunder_landing = (target["rect"].x+80,target["rect"].y+60)
                            draw(SCREEN,thunder_special_power["img"],thunder_landing)
                            el_cebolla["special_atk"] -= 5
                           
                            
                        turn_cooldown = 0
                        current_turn += 1
                elif turn_cooldown >= turn_wait_time:
                    draw_text(SCREEN,"FIN DEL TURNO",FONT,RED,(WIDTH//2,200))
                    turn_cooldown = 0
                    current_turn += 1

                if current_turn > 1:
                    for current_enemie in enemies[enemie_index][:]:
                        enemie_phase += 1
                        if current_turn == enemie_phase:
                            turn_cooldown += 1
                            if current_enemie["alive"] and turn_cooldown >= enemy_turn_wait_time:
                                animate_character(current_enemie,'a')
                                attack(current_enemie,el_cebolla)
                                turn_cooldown = 0
                                current_turn += 1
                            else:
                                enemy_focused +=1
                        elif enemie_phase > len(enemies[enemie_index]):
                            enemie_phase = 1



                total_turnos = len(enemies[enemie_index])+1            
                            
                if current_turn > total_turnos:
                    current_turn = 1
                    action_knight = False
                    atk_flag = True
                    potion_flag = True
                    special_flag = True
                    turn_cooldown = 0

                
                for i in range(len(enemies[enemie_index])):
                    altura_nombre = (i+1) *40
                    altura_barra_hp = i *45
                    draw(SCREEN,pygame.transform.flip(enemies[enemie_index][i]["animation"],True,False),enemies[enemie_index][i]["rect"])
                    write_panels(SCREEN,f"{enemies[enemie_index][i]["name"]} {enemies[enemie_index][i]["hp"]}",FONT,GREEN,(700,HEIGHT-PANEL_TOP + altura_nombre))
                    health_bar(SCREEN,enemies[enemie_index][i]["hp"],enemies[enemie_index][i]["max_hp"],altura_barra_hp,False )

                for current_enemie in enemies[enemie_index][:]:
                    if current_enemie["hp"] <= 0:
                        enemies[enemie_index].remove(current_enemie)
            else:
                

                return True


            draw(SCREEN,el_cebolla["animation"],el_cebolla["rect"])
            write_panels(SCREEN,f"El cebolla {el_cebolla["hp"]}",FONT,GREEN,(100,HEIGHT-PANEL_TOP + 40))
            health_bar(SCREEN,el_cebolla["hp"],el_cebolla["max_hp"],ALTURA_BARRA_HP_BATTLE)

            pygame.draw.rect(SCREEN,WHITE,attack_btn,1)
            pygame.draw.rect(SCREEN,WHITE,potion_btn,1)
            pygame.draw.rect(SCREEN,WHITE,huir_btn,1)
            pygame.draw.rect(SCREEN,WHITE,pass_btn,1)


        else:
            SCREEN.fill(BLACK)
            yes_btn = write_panels(SCREEN,"Yes",FONT,WHITE,(WIDTH//2-50,HEIGHT//2+100))
            no_btn = write_panels(SCREEN,"No",FONT,WHITE,(WIDTH//2+50,HEIGHT//2+100))
            draw_text(SCREEN,"GAME OVER",FONT,RED,SCREEN_CENTER)
            draw_text(SCREEN,"Continue?",FONT,RED,(WIDTH//2,HEIGHT//2 +60))
            pygame.draw.rect(SCREEN,WHITE,yes_btn,1)
            pygame.draw.rect(SCREEN,WHITE,no_btn,1)



        
        pygame.display.flip()


    

        


def main_gameplay_screen(SCREEN,map,battle = False):
    clock = pygame.time.Clock()

    
    move_down = False
    move_left = False
    move_right = False
    move_up = False
    movement_speed = 15

    spawn_heal = False
    spawn_energy = False

    SPAWNHEALEVENT = USEREVENT + 1 
    SPAWNENERGY = USEREVENT + 2

    pygame.time.set_timer(SPAWNHEALEVENT,5000)
    pygame.time.set_timer(SPAWNENERGY,7000)


    if map:
        pygame.mixer.music.load("./src/assets/audio/map_song.mp3")
        pygame.mixer.music.set_volume(MUSIC_VOLUME)
        pygame.mixer.music.play()



    while map:

        clock.tick(FPS)

        draw_bg_layers(SCREEN,scaled_bg_map,(0,0))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                    if evento.key == K_LEFT:
                        move_left = True
                        move_right = False

                    if evento.key == K_RIGHT:
                        move_right = True
                        move_left = False

                    if evento.key == K_UP:
                        move_up = True

                    if evento.key == K_DOWN:
                        move_down = True

            if evento.type == pygame.KEYUP:
                if evento.key == K_LEFT:
                    move_left = False

                if evento.key == K_RIGHT:
                    move_right = False

                if evento.key == K_UP:
                    move_up = False

                if evento.key == K_DOWN:
                    move_down = False
            
            if evento.type == SPAWNHEALEVENT:
                spawn_heal = True
            if evento.type == SPAWNENERGY:
                spawn_energy = True


        check_movement(move_left,move_right,move_up,move_down,el_cebolla,WIDTH,HEIGHT,movement_speed,SCREEN)


        for i in range(len(enemies)):

            draw_enemie_in_map(SCREEN,el_cebolla,enemies[i])

            
            for j in range(len(enemies[i])):
                if detectar_colision(el_cebolla["map_image_rect"], enemies[i][j]["map_image_rect"]):
                    enemie_index = i #indice del tipo de enemigo que colisiono
                    map = False
                    battle = True


        if spawn_heal:
            draw(SCREEN,extra_potion["img"],(100,320))
    
            if detectar_colision(el_cebolla["map_image_rect"],extra_potion["rect"]):  
                el_cebolla["potions"] += 1
                spawn_heal = False

        if spawn_energy:
            draw(SCREEN,energy_for_special["img"],(600,320))
            if detectar_colision(el_cebolla["map_image_rect"],energy_for_special["rect"]):
                el_cebolla["special_atk"] += 1 
                spawn_energy = False
                


        if el_cebolla["special_atk"] >=5:

            draw_text(SCREEN,"SPECIAL AVAILABLE",FONT,BLACK,ALTURA_SPECIAL_AVAILABLE)

        health_bar(SCREEN,el_cebolla["hp"],el_cebolla["max_hp"],ALTURA_BARRA_HP_MAP)

        if not final_boss["alive"]:
            SCREEN.fill(BLACK)
            draw_text(SCREEN,"END",FONT,WHITE,SCREEN_CENTER)
        

        pygame.display.flip()


    
    if not map:
        battle_screen(battle,SCREEN,enemie_index)
    
    if battle_screen(battle,SCREEN,enemie_index):
        battle = False
        map = True
        main_gameplay_screen(SCREEN,map,battle)