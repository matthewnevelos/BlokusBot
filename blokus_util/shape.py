import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm

class Shape():
    """
    Shape class, each unique shape will be instantiated from this

    Attributes:
    name : str
        name of shape
    tiles : np.ndarray
        (5,5) array with 1's indicating inner tiles, 2's indicating corner tiles. 0 elsewhere
    score : int
        number of tiles in the shape
        
    Methods:
    rotate():
        rotates tiles by 90 degrees clockwise about the center tile
    flip():
        flips tiles about (0,2) axes. (middle horizontal line) 
        - only useful for pieces without reflection symmetry
    _show_piece():
        debugging method to graphically show the piece
    """
    def __init__(self, name, inner_tiles, corner_tiles):
        """
        Instantiate shape object

        Parameters:
        name : str
            name of shape
        inner_tiles : List[Tuple] or None
            coordinates of non-corner tiles based on the center. The center of the tile which 
            is to be arbritrarily chosen is placed in the center (2,2)
        corner_tiles : List[Tuple]
            coordinates of the corner tiles based on the center
        """
        self.name = name
        self.tiles = np.zeros((5,5))
        if inner_tiles != None:
            for x,y in inner_tiles:
                self.tiles[x,y] = 1
        for x,y in corner_tiles:
            self.tiles[x,y] = 2
        self.score = np.count_nonzero(self.tiles)

    def rotate(self, k=1):
        self.tiles = np.rot90(self.tiles, k=k)

    def flip(self):
        self.tiles = np.flip(self.tiles, axis=0)

    def _show_piece(self):
        cmap = ListedColormap(['black', 'yellow', 'darkorange'])
        bounds = [0, 1, 2, 3]
        norm = BoundaryNorm(bounds, cmap.N)
        fig, ax = plt.subplots()
        plt.pcolormesh(self.tiles.reshape(5,5), norm=norm, cmap=cmap)
        major_ticks = np.arange(0, 5, 1)
        ax.grid()

        plt.xticks(major_ticks)
        plt.yticks(major_ticks)

        plt.show()

    def __getitem__(self):
        return self.name

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
    
    def __index__(self):
        return self.name
    
    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        if isinstance(other, Shape):
            return (self.name, self.tiles, self.score) == (other.name, other.tiles, other.score)

    

"""
No naming scheme for polyominoes, use your imagination and Shape._show_piece() to see which is which
1 Tile: i1
2 Tile: i2
3 Tile: i3, L3
4 Tile: i4, L4, T4, Z4, Sq
5 Tile: i5, L5, T5, Z5, P, X, Fz, V, y, U, W, eta
"""
def inititalize_shapes():
    #1 score pieces
    i1 = Shape('i1', None, [(2,2)])

    #2 score pieces
    i2 = Shape('i2', None, [(2,2), (2,3)])

    #3 score pieces
    i3 = Shape('i3', [(2,2)],
                     [(2,1), (2,3)])
    L3 = Shape('L3', None,
                     [(2,2), (2,3), (3,2)])

    #4 score pieces
    i4 = Shape('i4', [(2,2), (3,2)],
                     [(1,2), (4,2)])
    L4 = Shape('L4', [(2,2)],
                     [(2,3), (3,3), (2,1)])
    T4 = Shape('T4', [(2,3)],
                     [(2,2), (3,3), (1,3)])
    Z4 = Shape('Z4', None,
                     [(2,2), (3,2), (2,3), (1,3)])
    Sq = Shape('Sq', None,
                     [(2,2), (2,3), (3,2), (3,3)])
    
    #5 score pieces
    i5 = Shape('i5', [(2,2), (2,1), (2,3)],
                     [(2,0), (2,4)])
    L5 = Shape('L5', [(2,2), (2,3)],
                     [(2,1), (3,1), (2,4)])
    T5 = Shape('T5', [(2,2), (2,3)],
                     [(2,1), (3,3), (1,3)])
    Z5 = Shape('Z5', [(2,2)],
                     [(2,3), (2,1), (3,1), (1,3)])
    P = Shape('P',   [(2,2)],
                     [(2,3), (3,3), (3,2), (2,1)])
    X = Shape('X',   [(2,2)],
                     [(1,2), (3,2), (2,1), (2,3)])
    Fz = Shape('Fz', [(2,2)],
                     [(2,3), (2,1), (3,3), (1,2)])
    V = Shape('V',   [(2,3), (3,2)],
                     [(2,2), (4,2), (2,4)])
    y = Shape('y',   [(2,3), (2,2)],
                     [(2,1), (2,4), (1,3)])
    U = Shape('U',   [(2,2)],
                     [(3,2), (1,2), (3,3), (1,3)])
    W = Shape('W',   None,
                     [(2,2), (2,1), (1,2), (1,3), (3,1)])
    eta = Shape('eta', [(3,2)],
                         [(2,2), (4,2), (2,3), (1,3)])
    
    return [i1,i2,i3,L3,i4,L4,T4,Z4,Sq,i5,L5,T5,Z5,P,X,Fz,V,y,U,W,eta]


if __name__ == '__main__':
    shapes = inititalize_shapes()
    print(shapes.index('i2'))