import pytest
import pygame
import random
from pygame.locals import *

#from pygame.sprite import Group

# A world has a size
    # This impacts dimensions and sprite size
# Impassable Terrain
# Food Sources
# A world has a map
# A world has players
# A world is fullscreen

class World:
    def __init__(self):
        self.dimensions = (0,0)
        self.sprite_size = (0,0)
        self.food_coords = []
        self.map = None

    def set_dimensions(self,input):
        if input == 'small':
            self.dimensions = (50,50)
        elif input == 'medium':
            self.dimensions = (100,100)
        elif input == 'large':
            self.dimensions = (150,150)  
    
    def set_sprite_size(self,input):
        if input == 'small':
            self.sprite_size = (15,15)
        elif input == 'medium':
            self.sprite_size = (10,10)
        elif input == 'large':
            self.sprite_size = (5,5) 
    
    def generate_world(self,input):
        self.set_dimensions(input)
        self.set_sprite_size(input)

    def generate_food(self):
        for i in range(0, self.dimensions[0]):
            x = i
            y = random.randint(0,self.dimensions[1] - self.sprite_size[1])
            self.food_coords.append([x,y])

    def generate_map(self):
        self.map = pygame.display.set_mode(self.dimensions)
        self.map.fill((50,50,50))

    