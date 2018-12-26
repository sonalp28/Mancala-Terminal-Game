from minimax import *
from mancala import *
import decimal
decimal.getcontext().prec = 100
def g(b,nodes=0,depth = 0):
    mysum = 1
    for i in range(1, depth+1):
        mysum += b**i
    return mysum - (nodes+1)

def dg(b,depth=0):
    mysum = 1
    for i in range(1, depth):
        mysum += (i+1)*b*i
    return mysum

def newton(b0, g, dg,nodes=0,depth = 0):
    b = [b0]
    for n in range(0, 10):
        #print(b[n])
        #b.append( decimal.Decimal( b[n] - g(b[n],nodes,depth)/ dg(b[n],depth)) )
        b.append( b[n] - g(b[n],nodes,depth)/ dg(b[n],depth) )
    return b

def branchFactorCalculation(nodes=0,depth=0):
    optimal_b0 = (nodes+1)**(1./depth)
    b = newton(optimal_b0,g,dg,nodes,depth)
    return optimal_b0,b[-1]

def palyGrad(game,alg,moves=None,verbose=False):

    state = game.initial()
    player = game.player(state)
    turn = 0
    full_node_count = 0
    for move in count():

        if game.is_over(state): break
        if move == moves: break

        if player != game.player(state): turn += 1
        player = game.player(state)
        #score = game.score(state)
        utility, action, node_count = alg(game, state)
        if move == 0: full_node_count = node_count

        '''if verbose: print("Move %d, turn %d: Player %d's move = %d, utility = %d, score = %d"%(
            move, turn, player, action, utility, score))
        if verbose: print("")'''

        state = game.result(state, action)
        if verbose: print(game.string(state))

    if verbose: print("Final score: %d, node count = %d" % (game.score(state), full_node_count))
    return utility,node_count



def testMinimax_Game():
    #max_depth = 5
    moves = 1
    verbose=True


    size_board = [(2,1), (3,1), (3,2), (4,2), (5,3), (6,4)]
    maxdepth = [1,2,3,4,5,6,7,8]
    f = open('output_exper_grad_Minimax2.txt','w')
    for i in maxdepth:
        #alg = lambda game, state: minimax(game, state, max_depth=i)
        f.write(f'Depth is {i}\n')
        for size,count in size_board:
            mg = MancalaGame(size, count)
            initstate = mg.initial()
            fs,_,nc = minimax(mg,initstate,max_depth = i)
            optimal_bf,effective_bf = branchFactorCalculation(nc,i)
            #utilityScore,nc = palyGrad(mg, alg, moves=moves, verbose=False)
            #fs = play_minimax_ab(mg, max_depth=i, moves=moves, verbose=True)
            f.write(f'Size of board Size: {size} Count: {count}\n')
            f.write(f'Final Score is: {fs}\n')
            f.write(f'Node Count is: {nc}\n')
            f.write(f'BF using (N+1)**(1./d) is: {optimal_bf}\n')
            f.write(f'BF effective using newton is : {effective_bf}\n')




def testMinimax_ABGame():
    #max_depth = 5
    moves = 1
    verbose=True


    size_board = [(2,1), (3,1), (3,2), (4,2), (5,3), (6,4)]
    maxdepth = [1,2,3,4,5,6,7,8]
    f = open('output_exper_grad_AB2.txt','w')
    for i in maxdepth:
        #alg = lambda game, state: minimax(game, state, max_depth=i)
        f.write(f'Depth is {i}\n')
        for size,count in size_board:
            mg = MancalaGame(size, count)
            initstate = mg.initial()
            fs,_,nc = minimax_ab(mg,initstate,max_depth=i)
            optimal_bf,effective_bf = branchFactorCalculation(nc,i)
            #utilityScore,nc = palyGrad(mg, alg, moves=moves, verbose=False)
            #fs = play_minimax_ab(mg, max_depth=i, moves=moves, verbose=True)
            f.write(f'Size of board Size: {size} Count: {count}\n')
            f.write(f'Final Score is: {fs}\n')
            f.write(f'Node Count is: {nc}\n')
            f.write(f'Branch factor using formula (N+1)/d is: {optimal_bf}\n')
            f.write(f'Branch factor effective using formula newton is : {effective_bf}\n')


testMinimax_Game()
testMinimax_ABGame()
