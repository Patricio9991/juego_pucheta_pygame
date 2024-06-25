import pygame
import os

class Knight():
    def __init__(self, x,y,name,max_hp,str,potions):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.str = str
        self.start_potions = potions
        self.potions = potions
        self.alive = True
        self.animation_list = []
        self.current_frame = 0
        for i in range(1,9):
            img = pygame.image.load(f'./assets/knight/Idle/Idle_{i}.png')
            img = pygame.transform.scale(img, (img.get_width()*3, img.get_height()*3))
            self.animation_list.append(img)
        self.image = self.animation_list[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def draw(self,screen):
        screen.blit(self.image,self.rect)

    def draw_flip(self,screen,corrdenadas):
        screen.blit(pygame.transform.flip(self.image,True,False),corrdenadas)

    def update(self):
        self.current_frame += 0.1

        if self.current_frame >= len(self.animation_list):
            self.current_frame = 0

        self.image = self.animation_list[int(self.current_frame)]    

class Skeleton:
    def __init__(self, x,y,name,max_hp,str,potions):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.str = str
        self.start_potions = potions
        self.potions = potions
        self.alive = True
        self.animation_list = []
        self.current_frame = 0
        for i in range(1,5):
            img = pygame.image.load(f'./assets/skeleton/Idle/Idle_{i}.png')
            img = pygame.transform.scale(img, (img.get_width()*3, img.get_height()*3))
            self.animation_list.append(img)
        self.image = self.animation_list[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def draw(self,screen):
        screen.blit(self.image,self.rect)

    def update(self):
        self.current_frame += 0.1

        if self.current_frame >= len(self.animation_list):
            self.current_frame = 0

        self.image = self.animation_list[int(self.current_frame)] 


files = os.listdir('./assets/skeleton/Idle')

print(files)