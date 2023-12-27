import numpy as np
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt

def setup():
    #Initialize board
    board = np.zeros(8*8)

    #Player colour is yellow
    #Opp colour is red
    cmap_colors = [
    (0.0, 'black'),
    (0.33, 'white'),
    (0.66, 'yellow'),
    (1.0, 'red')]

    custom_cmap = LinearSegmentedColormap.from_list('custom_colormap', cmap_colors)

    return board, custom_cmap

def show_board(board):
    fig, ax = plt.subplots()
    ax.pcolormesh(board, cmap=board_colours)
    ax.invert_yaxis()
    ax.set_aspect('equal')
    ax.grid()
    fig.show()


start_board, board_colours = setup()
