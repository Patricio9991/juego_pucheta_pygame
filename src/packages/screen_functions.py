import pygame


def draw(screen,img,coordenadas):
    screen.blit(img, coordenadas)

def draw_text(screen,text,font,text_col,x,y):
    render_font = font.render(text,True,text_col)
    screen.blit(render_font,(x,y))


def write_panels(screen,text,font,color,x,y):

    draw_text(screen,text,font,color,x,y)



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

    

    folder_items = os.listdir(f'./assets/{folder_name}')



    for i in range(len(folder_items)):
        sub_carpeta_items = os.listdir(f'./assets/{folder_name}/{folder_items[i]}')
        aux_lista_imagenes = []
     

        for j in range(len(sub_carpeta_items)):
            
            img = pygame.image.load(f'./assets/{folder_name}/{folder_items[i]}/{sub_carpeta_items[j]}')
            img = pygame.transform.scale(img, (img.get_width()*3, img.get_height()*3))
            aux_lista_imagenes.append(img)
          
        
        lista_imagenes.append(aux_lista_imagenes)
    
    return lista_imagenes




