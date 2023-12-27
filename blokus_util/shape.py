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
        rotates tiles by 90 degrees counter clockwise about the center tile
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
        inner_tiles : List[Tuple]
            coordinates of non-corner tiles based on the center. The center of the tile which 
            is to be arbritrarily chosen is placed in the center (2,2)
        corner_tiles : List[Tuple]
            coordinates of the corner tiles based on the center
        """
        self.name = name
        self.tiles = np.zeros((5,5))
        for x,y in inner_tiles:
            self.tiles[x,y] = 1
        for x,y in corner_tiles:
            self.tiles[x,y] = 2
        self.score = np.count_nonzero(self.tiles)

    def rotate(self, k=1):
        self.tiles = np.rot90(self.tiles, k=k)

    def flip(self):
        pass

    def _show_piece(self):
        cmap = ListedColormap(['black', 'yellow', 'darkorange'])
        bounds = [0, 1, 2, 3]
        norm = BoundaryNorm(bounds, cmap.N)
        fig, ax = plt.subplots()
        plt.pcolormesh(self.tiles.reshape(5,5), norm=norm, cmap=cmap)
        major_ticks = np.arange(0, 5, 1)
        ax.set_xticks(major_ticks)
        ax.set_yticks(major_ticks)
        ax.grid()

        plt.show()


if __name__ == '__main__':
    m = [(2,2), (3,2)]
    c = [(4,2)]
    shape = Shape('shape1', m, c)
    shape._show_piece()
    print(shape.__dict__)