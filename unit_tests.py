import pytest
import pygame
from pygame.locals import *
from world import World as world
from play import *

class TestWorldClass:

    def setup(self):
        self.world = world()

    def test_world_dimensions(self):
        assert self.world.dimensions == (0,0)
        
    def test_world_sprize_size(self):
        assert self.world.sprite_size == (0,0)


    def test_set_world_dimension_small_dimension(self):
        input = 'small'
        self.world.set_dimensions(input)
        assert self.world.dimensions == (50,50)

    def test_set_world_dimension_medium_dimension(self):
        input = 'medium'
        self.world.set_dimensions(input)
        assert self.world.dimensions == (100,100)

    def test_set_world_dimension_large_dimension(self):
        input = 'large'
        self.world.set_dimensions(input)
        assert self.world.dimensions == (150,150)


    def test_set_world_dimension_small_sprite(self):
        input = 'small'
        self.world.set_sprite_size(input)
        assert self.world.sprite_size == (15,15)

    def test_set_world_dimension_medium_sprite(self):
        input = 'medium'
        self.world.set_sprite_size(input)
        assert self.world.sprite_size == (10,10)

    def test_set_world_dimension_large_sprite(self):
        input = 'large'
        self.world.set_sprite_size(input)
        assert self.world.sprite_size == (5,5)

    def test_generate_world_small(self):
        input = 'small'
        self.world.generate_world(input)
        assert self.world.sprite_size == (15,15)
        assert self.world.dimensions == (50,50)

    def test_generate_world_medium(self):
        input = 'medium'
        self.world.generate_world(input)
        assert self.world.sprite_size == (10,10)
        assert self.world.dimensions == (100,100)

    def test_generate_world_large(self):
        input = 'large'
        self.world.generate_world(input)
        assert self.world.sprite_size == (5,5)
        assert self.world.dimensions == (150,150)


class TestSmallWorldClass:

    def setup(self):
        self.world = world()
        self.world.generate_world('small')

    def test_generate_random_food(self):
        self.world.generate_food()
        assert self.world.food_coords != []

    def test_accurate_food_count(self):
        self.world.generate_food()
        assert len(self.world.food_coords) == 50

    def test_generate_map(self):
        self.world.generate_map()
        assert self.world.map != None
    


class TestMediumWorldClass:

    def setup(self):
        self.world = world()
        self.world.generate_world('medium')

    def test_generate_random_food(self):
        self.world.generate_food()
        assert self.world.food_coords != []
    
    def test_accurate_food_count(self):
        self.world.generate_food()
        assert len(self.world.food_coords) == 100

    def test_generate_map(self):
        self.world.generate_map()
        assert self.world.map != None


class TestLargeWorldClass:

    def setup(self):
        self.world = world()
        self.world.generate_world('large')

    def test_generate_random_food(self):
        self.world.generate_food()
        assert self.world.food_coords != []

    def test_accurate_food_count(self):
        self.world.generate_food()
        assert len(self.world.food_coords) == 150

    def test_generate_map(self):
        self.world.generate_map()
        assert self.world.map != None

class TestGameLoop:

    def setup(self):
        start_game()

    def test_start_game(self):
        assert pygame.get_init() == True
    
    def test_end_game(self):
        end_game()
        assert pygame.get_init() == False

    def test_start_and_end_game(self):
        assert pygame.get_init() == True
        end_game()
        assert pygame.get_init() == False

    def test_create_display(self):
        test_world = create_display(input)
        assert isinstance(test_world, world) 

    def test_create_display(self):
        test_world = create_display(input)
        assert isinstance(test_world, world) 

class TestGameDisplay:

    def setup(self):
        start_game()
        open_display()

    def test_start_and_open_display(self):
        assert pygame.display.get_init() == True

    def test_open_and_close_display(self):
        close_display()
        assert pygame.display.get_init() == False

    def test_create_display_small(self):
        input = 'small'
        test_world = create_display(input)
        assert isinstance(test_world, world) 

    def test_create_display_medium(self):
        input = 'medium'
        test_world = create_display(input)
        assert isinstance(test_world, world) 

    def test_create_display_large(self):
        input = 'large'
        test_world = create_display(input)
        assert isinstance(test_world, world) 


class TestStartGameMakeWorld:

    def setup(self):
        start_game()
        self.world = world()

    def test_start_game_create_world(self):
        assert self.world.dimensions == (0,0)

    def test_start_game_create_world_with_dimensions(self):
        input = 'small'
        self.world.generate_world(input)
        assert self.world.sprite_size == (15,15)
        assert self.world.dimensions == (50,50)

    def test_start_game_create_world_map(self):
        input = 'small'
        self.world.generate_world(input)
        self.world.generate_map()
        assert self.world.map != None