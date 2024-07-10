from packages.character_functions import *
from settings import SPECIAL_ITEM_SIZE, SPECIAL_THUNDER_SIZE



imagenes = cargar_imagenes("items")

energy_img = imagenes[0][0]
scale_energy_img = scale_image(SPECIAL_ITEM_SIZE,energy_img)
energy_for_special = extra_item(600,320,scale_energy_img)

potion_img = imagenes[0][1]
scaled_potion_img = scale_image(SPECIAL_ITEM_SIZE,potion_img)
extra_potion = extra_item(100,320,scaled_potion_img)

thunder_img = imagenes[0][2]
scaled_thunder_img = scale_image(SPECIAL_THUNDER_SIZE,thunder_img)
thunder_special_power = special_power(100,320,scaled_thunder_img)






