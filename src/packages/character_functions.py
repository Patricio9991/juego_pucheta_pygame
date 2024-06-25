import pygame


def new_personaje(x,y,nombre,hp,max_hp,str,potions,alive,animation_list):

    personaje = {
        "name":nombre,
        "hp":hp,
        "max_hp":max_hp,
        "str": str,
        "start_potions": potions,
        "potions": potions,
        "alive": alive,
        "animation_list": animation_list,
        "current_frame": 0,
        "animation":animation_list[0][0],
        "rect": animation_list[0][0].get_rect()
    }

    personaje["rect"].center = (x,y)
    

    return personaje



def animate_character(personaje,accion = None):
        personaje["current_frame"] += 0.1

        match accion:
            case 'a':
                personaje['animation_list'][1]

                if personaje["current_frame"] >= len(personaje["animation_list"][1]):
                    personaje["current_frame"]  = 0
                    
                personaje["animation"] = personaje["animation_list"][1][int(personaje["current_frame"])] 
            case _:
                personaje['animation_list'][0]

                if personaje["current_frame"] >= len(personaje["animation_list"][0]):
                    personaje["current_frame"]  = 0
                    
                personaje["animation"] = personaje["animation_list"][0][int(personaje["current_frame"])] 


def health_bar(screen,hp,max_hp,player = True):
    damage = hp / max_hp

    if player:
        red_bar = pygame.rect.Rect(30,520,150,20)
        green_bar = pygame.rect.Rect(30,520,150 * damage,20)

        pygame.draw.rect(screen,(255,0,0),red_bar)
        pygame.draw.rect(screen,(0,255,0),green_bar)

    else:
        red_bar = pygame.rect.Rect(620,520,150,20)
        green_bar = pygame.rect.Rect(620,520,150 * damage,20)

        pygame.draw.rect(screen,(255,0,0),red_bar)
        pygame.draw.rect(screen,(0,255,0),green_bar)

         

    