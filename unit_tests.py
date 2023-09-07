import pytest
from world import World as world

class TestClass:

    def setup(self):
        self.world = world()

    def test_world_dimensions(self):
        assert self.world.dimensions == (0,0)

    def test_set_world_dimension_small(self):
        input = 'small'
        self.world.set_dimensions(input)
        assert self.world.dimensions == (50,50)

    def test_set_world_dimension_medium(self):
        input = 'medium'
        self.world.set_dimensions(input)
        assert self.world.dimensions == (100,100)

    def test_set_world_dimension_large(self):
        input = 'large'
        self.world.set_dimensions(input)
        assert self.world.dimensions == (150,150)