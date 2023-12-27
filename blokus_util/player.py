import numpy as np

def i2xy(i):
    #i = index of array (0-143)
    if i < 144:
        x = i % 12
        y = i // 12 
        return x, y
    else:
        raise(IndexError("Index must be less than number of tiles."))


def xy2i(x, y):
    #x, y are coordinates of board (0-11)
    if (0 <= x <= 11 and 0 <= y <= 11):
        i = y * 12 + x
        return i
    else:        
        raise(IndexError("x and y must be in range (0-11)"))

def available_tile(board):
    for i in range(board.size):
        if board[i] == 0:
            x, y = i2xy(i)
            if (1 <= x <= 10 and 1 <= y <= 10):
                sides = board[[xy2i(x-1, y), xy2i(x+1, y), xy2i(x, y-1), xy2i(x, y+1)]]
                corners = board[[xy2i(x-1, y-1), xy2i(x+1, y+1), xy2i(x+1, y-1), xy2i(x-1, y+1)]]
                if np.all(sides != 1):
                    if np.any(corners == 1):
                        board[i] = 2
            elif (x==0 and (1 <= y <= 10)):
                sides = board[[xy2i(x+1, y), xy2i(x, y-1), xy2i(x, y+1)]]
                corners = board[[xy2i(x+1, y+1), xy2i(x+1, y-1)]]
                if np.all(sides != 1):
                    if np.any(corners == 1):
                        board[i] = 2
            elif (x==11 and (1 <= y <= 10)):
                sides = board[[xy2i(x-1, y), xy2i(x, y-1), xy2i(x, y+1)]]
                corners = board[[xy2i(x-1, y-1), xy2i(x-1, y+1)]]
                if np.all(sides != 1):
                    if np.any(corners == 1):
                        board[i] = 2
            elif(y==0 and (1<= x <= 10)):
                sides = board[[xy2i(x-1, y), xy2i(x+1, y), xy2i(x, y+1)]]
                corners = board[[xy2i(x+1, y+1), xy2i(x-1, y+1)]]
                if np.all(sides != 1):
                    if np.any(corners == 1):
                        board[i] = 2
            elif(y==11 and (1<= x <= 10)):
                sides = board[[xy2i(x-1, y), xy2i(x+1, y), xy2i(x, y-1)]]
                corners = board[[xy2i(x-1, y-1), xy2i(x+1, y-1)]]
                if np.all(sides != 1):
                    if np.any(corners == 1):
                        board[i] = 2
    return board


if __name__ == '__main__':
    board = np.zeros(12*12)
    board[[1,2,3,4,5,51]] = [1,1,1,0,1,-1]
    board = available_tile(board)

# def check_valid(board, shape):

