import pygame


def draw(screen,img,coordenadas):
    screen.blit(img, coordenadas)

def draw_text(screen,text,font,text_col,coordenada):
    render_font = font.render(text,True,text_col)
    rect = render_font.get_rect()
    rect.center = coordenada
   
    screen.blit(render_font,rect)

    return rect


def write_panels(screen,text,font,color,coordenada):

    return draw_text(screen,text,font,color,coordenada)



def draw_bg_layers(screen,bg_list,coordenadas):

    for i in range(len(bg_list)):
        screen.blit(bg_list[i], coordenadas)
        
def scale_image(new_size,images):
    scaled_images = []
    for i in range(len(images)):
        scaled_images.append(pygame.transform.scale(images[i],new_size))
    
    return scaled_images



def cargar_imagenes(folder_name):
    import os

    lista_imagenes = []

    

    folder_items = os.listdir(f'./src/assets/{folder_name}')



    for i in range(len(folder_items)):
        sub_carpeta_items = os.listdir(f'./src/assets/{folder_name}/{folder_items[i]}')
        aux_lista_imagenes = []
     

        for j in range(len(sub_carpeta_items)):
            
            img = pygame.image.load(f'./src/assets/{folder_name}/{folder_items[i]}/{sub_carpeta_items[j]}').convert_alpha()
            img = pygame.transform.scale(img, (img.get_width()*3, img.get_height()*3))
            aux_lista_imagenes.append(img)
          
        
        lista_imagenes.append(aux_lista_imagenes)
    
    return lista_imagenes


def distancia_entre_puntos(punto_1:tuple[int,int],punto_2:tuple[int,int]) -> float:


    x1,y1 = punto_1
    x2,y2 = punto_2


    return ((x2-x1)**2 + (y2-y1)**2) ** 0.5


def calcular_radio(rect):
    return rect.width //2



def detectar_colision_circulo(rect1,rect2)->bool:
    

    r1 = calcular_radio(rect1)
    r2 = calcular_radio(rect2)

    distancia = distancia_entre_puntos(rect1.center,rect2.center)

    return  distancia <= r1+r2


def punto_en_rectangulo(punto,rect)->bool:

    return punto[0] >= rect.left and punto[0] <= rect.right and punto[1] >= rect.top and punto[1] <= rect.bottom
