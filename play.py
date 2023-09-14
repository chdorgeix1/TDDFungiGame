import pytest
import pygame
import random
from world import World as world
from pygame.locals import *

def start_game():
    pygame.init()

def end_game():
    pygame.quit()

def open_display():
    pygame.display.init()

def close_display():
    pygame.display.quit()

def create_display(world_size):
    game_world = world()
    game_world.generate_world(world_size)
    game_world.generate_map()
    return game_world

# def continue_game():
#     running = True
#     while running:
    
#         #  for loop through the event queue  
#         for event in pygame.event.get():
        
#             # Check for QUIT event      
#             if event.type == pygame.QUIT:
#                 running = False

# start_game()
# # open_display()
# create_display()
# continue_game()