import pytest
#import pygame
import random
#from pygame.sprite import Group

# A world has a size
    # This impacts dimensions and sprite size
# Impassable Terrain
# Food Sources


class World:
    def __init__(self):
        self.dimensions = (0,0)

    def set_dimensions(self,input):
        if input == 'small':
            self.dimensions = (50,50)
        elif input == 'medium':
            self.dimensions = (100,100)
        elif input == 'large':
            self.dimensions = (150,150)  