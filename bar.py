# Class file for the bar

###############
### Imports ###
###############
import pygame
from settings import *

#################
### Bar Class ###
#################
class Bar:
    def __init__(self, bar_height, num_of_bars):
        self.inner_width = width / num_of_bars - 10
        self.width = width / num_of_bars
        self.height = bar_height
        self.colour = grey

    def is_sorting(self):
        return self.colour == green

    def is_sorted(self):
        return self.colour == red

    def is_unsorted(self):
        return self.colour == grey

    def is_minimum(self):
        return self.colour == blue

    def make_sorting(self):
        self.colour = green

    def make_sorted(self):
        self.colour = red

    def make_unsorted(self):
        self.colour = grey

    def make_minimum(self):
        self.colour = blue

    def draw(self, screen, x, y):
        pygame.draw.rect(screen, self.colour, (x, y, self.inner_width, self.height))        

    def __gt__(self, other):
        return self.height > other.height

    def __lt__(self, other):
        return self.height < other.height

