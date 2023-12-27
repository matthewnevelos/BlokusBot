import numpy as np
from matplotlib.colors import ListedColormap, BoundaryNorm
import matplotlib.pyplot as plt


def board_colors():
    custom_cmap = ListedColormap(['red', 'black', 'white', 'yellow'])
    bounds = [-1, 0, 1, 2, 3]
    norm = BoundaryNorm(bounds, custom_cmap.N)
    return custom_cmap, norm

#execute on import and main
cmap, norm = board_colors()

def show_board(board, cmap=cmap, norm=norm):
    """
    board shape is (144,)
    """
    fig, ax = plt.subplots()
    plt.pcolormesh(board.reshape(12,12), cmap=cmap, norm=norm)

    major_ticks = np.arange(0, 13, 1)
    ax.set_xticks(major_ticks)
    ax.set_yticks(major_ticks)
    ax.grid(alpha=0.5)

    ax.set_aspect('equal')
    cbar = plt.colorbar(ticks=[-0.5, 0.5, 1.5, 2.5])
    cbar.set_ticklabels(['Opponent', 'Empty', 'Player', 'Possible'])
    
    plt.show()




#Only execute if main
if __name__ == '__main__':


    board = np.zeros((12,12))
    board[4] = 2
    board[0,0] = 1
    board = board.flatten()
    show_board(board, cmap, norm)