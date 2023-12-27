import pytest
from blokus_util import player


#xy2i
def test_player_xy2i():
    assert player.xy2i(4,5) == 64

def test_player_xy2i_x_error():
    with pytest.raises(IndexError):
        player.xy2i(15, 2)

def test_player_xy2i_y_error():
    with pytest.raises(IndexError):
        player.xy2i(1, 12)

#i2xy
def test_player_i2xy():
    assert player.i2xy(64) == (4, 5)

def test_player_i2xy_error():
    with pytest.raises(IndexError):
        player.i2xy(150)

        

