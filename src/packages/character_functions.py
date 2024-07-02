import pygame
from random import *
from settings import *

def new_personaje(x,y,nombre,hp,max_hp,str,potions,alive,animation_list):
    
    personaje = {
        "name":nombre,
        "hp":hp,
        "max_hp":max_hp,
        "str": str,
        "start_potions": potions,
        "potions": potions,
        "alive": alive,
        "current_frame": 0,
        "animation_list": animation_list,
        "map_image":animation_list[0][0],
        "map_image_rect": animation_list[0][0].get_rect(),
        "animation":animation_list[1][0],
        "rect": animation_list[1][0].get_rect(),
    }
    personaje["rect"].center = x,y
    

    
    

    return personaje

def load_enemie_list(lista_enemigos:list,nombre_enemigo:str,lista_animaciones:list,cantidad:int):
    enemie_width = 150
    enemie_height = 150
    

    for _ in range(cantidad):
        lista_enemigos.append(new_personaje(randint(0,WIDTH-enemie_width),randint(0,HEIGHT-enemie_height),nombre_enemigo,randint(0,50),50,randint(0,10),randint(0,3),True,lista_animaciones))

def animate_character(personaje,accion = None):
    
    frame = 1
    
    match accion:
        case 'a':
            frame += 1
            if frame >= len(personaje["animation_list"][2]):
                frame = 0

            personaje["animation"] = personaje["animation_list"][2][int(frame)] 

            
            
        case 'i':
            personaje["current_frame"] += 1
            if personaje["current_frame"] >= len(personaje["animation_list"][1]):
                personaje["current_frame"] = 0
                
            
            personaje["animation"] = personaje["animation_list"][1][int(personaje["current_frame"])] 

        
                        
                    

        
        





def health_bar(screen,hp,max_hp,altura = 0,player = True):
    damage = hp / max_hp

    if player:
        red_bar = pygame.rect.Rect(30,520,150,20)
        green_bar = pygame.rect.Rect(30,520,150 * damage,20)

        pygame.draw.rect(screen,(255,0,0),red_bar)
        pygame.draw.rect(screen,(0,255,0),green_bar)

    else:
        red_bar = pygame.rect.Rect(620,500 + altura,150,20)
        green_bar = pygame.rect.Rect(620,500 + altura,150 * damage,20)

        pygame.draw.rect(screen,(255,0,0),red_bar)
        pygame.draw.rect(screen,(0,255,0),green_bar)

         


def attack(pj,target):
    

    damage_total = pj["str"]

    target["hp"] -= damage_total

    if target['hp']<1:
        target['hp'] = 0
        target['alive'] = False

def heal(pj):
    restore_points = 10
    if pj["potions"]:
        pj["potions"] =-1

        if pj["hp"]+ restore_points < pj["max_hp"]:
            pj["hp"] += restore_points
        elif pj["hp"] + restore_points >= pj["max_hp"]:
            pj["hp"] = pj["max_hp"]
        

def wait_user(tecla):
    continuar = True
    while continuar:
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.type == pygame.QUIT:
                    continuar = False
                if evento.key == tecla:
                    continuar = False


