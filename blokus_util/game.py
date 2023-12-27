import numpy as np
from matplotlib.colors import ListedColormap, BoundaryNorm
import matplotlib.pyplot as plt


def board_colors():
    custom_cmap = ListedColormap(['red', 'black', 'white', 'yellow'])
    bounds = [-1, 0, 1, 2, 3]
    norm = BoundaryNorm(bounds, custom_cmap.N)
    return custom_cmap, norm

def show_board(board, cmap, norm):
    fig, ax = plt.subplots()
    plt.pcolormesh(board.reshape(8,8), cmap=cmap, norm=norm)
    ax.invert_yaxis()
    ax.set_aspect('equal')
    ax.grid()
    cbar = plt.colorbar(ticks=[-0.5, 0.5, 1.5, 2.5])
    cbar.set_ticklabels(['Opponent', 'Empty', 'Player', 'Possible'])
    
    plt.show()


#execute on import and main
cmap, norm = board_colors()


#Only execute if main
if __name__ == '__main__':


    board = np.zeros((8,8))
    board[4] = 2
    board[0,0] = 1
    board = board.flatten()
    show_board(board, cmap, norm)