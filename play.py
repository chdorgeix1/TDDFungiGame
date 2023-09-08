import pytest
import pygame
import random
from pygame.locals import *

def start_game():
    pygame.init()

def end_game():
    pygame.quit()

def open_display():
    pygame.display.init()

def close_display():
    pygame.display.quit()