from minimax import *
from mancala import *

def testMinimaxGame():
    max_depth = 5
    moves = 100
    verbose=True
    size_board = [(2,1), (3,1), (3,2), (4,2), (5,3), (6,4)]
    max_depth = [1,2,3,4,5,6,7,8]
    f = open('output.txt','w')
    for i in max_depth:
        f.write(f'Depth is {i}\n')
        for size,count in size_board:
            mg = MancalaGame(size, count)

            fs = play_minimax(mg, max_depth=i, moves=moves, verbose=False)
            f.write(f'Size of board Size: {size} Count: {count}\n')
            f.write(f'Final Score is: {fs}\n')

testMinimaxGame()
