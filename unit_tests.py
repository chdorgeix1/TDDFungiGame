import pytest
from world import World as world

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
