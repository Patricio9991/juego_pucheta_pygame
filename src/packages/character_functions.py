import pygame
from random import *
from settings import *
from packages.screen_functions import *

def new_personaje(x:int,y:int,nombre:str,hp:int,max_hp:int,str:int,potions:int,alive:bool,animation_list:list)->dict:
    """Crea un nuevo personaje

    Args:
        x (int): coordenada para el centro del rectangulo
        y (int): coordenada para el centro del rectangulo
        nombre (str): nombre del personaje
        hp (int): hp inicial del personaje
        max_hp (int): maxima hp del personaje
        str (int): fuerza del personaje
        potions (int): pociones iniciales
        alive (bool): Estado de vida o muerte
        animation_list (list): lista de animaciones

    Returns:
        dict: retorna un diccionario con el personaje creado
    """
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
        "map_image":pygame.transform.scale(animation_list[0][0],MAP_CHARACTER_SIZE),
        "map_image_rect": pygame.transform.scale(animation_list[0][0],MAP_CHARACTER_SIZE).get_rect(),
        "animation":animation_list[1][0],
        "rect": animation_list[1][0].get_rect(),
        "special_atk": 5
    }
    personaje["rect"].center = x,y
    personaje["map_image_rect"].x = randint(0, WIDTH - personaje["map_image_rect"].right)
    personaje["map_image_rect"].y = randint(0, HEIGHT - personaje["map_image_rect"].bottom)
    
    

    return personaje


def extra_item(x,y,img):
    item = {
        "coordenada_x" : x,
        "coordenada_y" : y,
        "img":img,
        "rect" : img.get_rect()
    }

    item["rect"].center = x,y

    return item

def special_power(x,y,img):
    return extra_item(x,y,img)


def animate_character(personaje:dict,accion:bool = None):
    """Anima un personaje segun parametro accion
        'a': Atacar
        'i': Idle
        'm': Muerte
        'c': Caminar
    Args:
        personaje (dict): recibe un diccionario de personaje
        accion (bool, optional): recibe una accion a,i,m,c. none por defecto
    """
    
    frame = 1
    
    match accion:
        case 'a':
            frame += 1
            if frame >= len(personaje["animation_list"][2]):
                frame = 0

            personaje["animation"] = personaje["animation_list"][2][frame] 

            
            
        case 'i':
            personaje["current_frame"] += 1
            if personaje["current_frame"] >= len(personaje["animation_list"][1]):
                personaje["current_frame"] = 0
                
            
            personaje["animation"] = personaje["animation_list"][1][int(personaje["current_frame"])] 

        
                        
                    

def health_bar(screen:pygame.Surface,hp:int,max_hp:int,altura:int = 0,player:bool = True)->None:

    """Dibuja una barra de vida para los personajes. Esta varia segun el daño recibido porcentualmente segun su hp actual y la cantidad maxima de hp que tiene

    Args:
        screen: surface de pygame
        hp(int): cantidad de hp actual
        max_hp(int): cantidad de vida maxima
        altura(int): altura de donde dibujar la barra de vida enemiga
        player(bool): sector de la pantalla donde se va a dibujar la barra de hp. True izquieda (jugador) False(derecha) enemigo.

    """
 

    damage = hp / max_hp

    if player:
        red_bar = pygame.rect.Rect(30,altura,150,20)
        green_bar = pygame.rect.Rect(30,altura,150 * damage,20)

        pygame.draw.rect(screen,(255,0,0),red_bar)
        pygame.draw.rect(screen,(0,255,0),green_bar)

    else:
        red_bar = pygame.rect.Rect(620,500 + altura,150,20)
        green_bar = pygame.rect.Rect(620,500 + altura,150 * damage,20)

        pygame.draw.rect(screen,(255,0,0),red_bar)
        pygame.draw.rect(screen,(0,255,0),green_bar)

         


def attack(pj:dict,target:dict,special = False)->None:
    """Funcion que calcula el daño de un personaje cuando a ataca a otro

    Args:
        pj (dict): diccionario de personaje atacante
        target (dict): diccionario de personaje objetivo
        special (bool): Cuando es ataque especial. Hace mas daño
    """

    damage_normal = pj["str"]
    damage_special = damage_normal + 30

    if special:
        target["hp"] -= damage_special
    else:
        target["hp"] -= damage_normal
    
    if target['hp']<1:
        target['hp'] = 0
        target['alive'] = False

def heal(pj:dict)->None:
    """_Funcion para utlizar posiones y recuperar la salud

    Args:
        pj (dict): diccionario de personaje que utiliza la key/value de las posiones para aumentar la salud del personaje
    """
    restore_points = 20
    if pj["potions"]:
        pj["potions"] -=1

        if pj["hp"] + restore_points < pj["max_hp"]:
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



def draw_enemie_in_map(screen:pygame.Surface,pj:dict,enemie_list:list[list])->None:
    """Dinuja en la pantalla a los enemigos
        [0]: esqueletos
        [1]: ojo volador
        [2]: jefe final

    Args:
        screen (pygame.Surface): Screen donde se va a dibujar
        pj (dict): diccionario con la informacion del personaje
        enemie_list (list[list]): lista que contiene una lista de enemigos
    """
    for i  in range(len(enemie_list)):
        draw(screen,enemie_list[i]["map_image"],enemie_list[i]["map_image_rect"])




def check_movement(left,right,top,bottom,rect,width,heigth,speed,SCREEN):
    
        
    if right and rect["map_image_rect"].right < width:
        if rect["map_image_rect"].right > width:
            rect["map_image_rect"].right = width
        rect["map_image_rect"].right += speed
    
    if left and rect["map_image_rect"].left > 0:
        if rect["map_image_rect"].left < 0:
            rect["map_image_rect"].left = 0
        rect["map_image_rect"].left -= speed

    if bottom and rect["map_image_rect"].bottom < heigth:
        if rect["map_image_rect"].bottom > heigth:
            rect["map_image_rect"].bottom = heigth
        print(rect["map_image_rect"].bottom)
        rect["map_image_rect"].bottom += speed
    
    if top and rect["map_image_rect"].top > 0:
        print(rect["map_image_rect"].top)
        if rect["map_image_rect"].top < 0:
            rect["map_image_rect"].top = 100
        rect["map_image_rect"].top -= speed


    
    if left:
        draw(SCREEN,pygame.transform.flip(rect["map_image"],True,False),rect["map_image_rect"])
    else:
        draw(SCREEN,rect["map_image"],rect["map_image_rect"])
    


