import numpy as np
class Shape():
    def __init__(self):
        self.points = None
    
    def tiles(self, x, y):
        self.tiles = [x+1, x-1, y+1, y-1]

class X(Shape):
    def __init__(self):
        self.points = 5
