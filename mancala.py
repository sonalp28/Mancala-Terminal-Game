"""
A game state is represented by a tuple.  The leading elements of
the tuple are the number of stones in each position, from position 0
to the final position. The last element of the tuple is the current
player, either 0 or 1.
"""

class MancalaGame:

    def __init__(self, size=6, count=4):
        self.size = size
        self.count = count

    def initial(self):
        """
        Return the initial game state.
        """
        return ((self.count,)*self.size + (0,))*2 + (0,)

    def player(self, state):
        """
        Return the current player in the given game state.
        """
        return state[-1]

    def actions(self, state):
        """"
        Return a list of all actions available in the current game state.
        Each action is the position number of a non-empty small position
        on the current player's half of the board.
        """
        permited_action = []
        if state[-1] == 0:
            for i in range(0, self.size):
                if state[i] != 0:
                    permited_action.append(i)
        if state[-1] == 1:
            for i in range(self.size + 1, len(state) - 2):#0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
                if state[i] != 0:
                    permited_action.append(i)
        return permited_action
        ## Finish me! ##
        #raise(Exception("Not implemented yet."))

    def result(self, state, action):
        """
        Return the new game state that results from playing the given
        action in the given state.  Be sure to account for the special
        cases where a player's last stone lands in one of their own small
        positions, and when a player's last stone lands in their own mancala.
        """
        ## Finish me! ##
        state_list = list(state)
        #print(" ")
        #print(state)
        #print(action)
        length = len(state_list)
        if state_list[-1] == 0:                                                           #logic for Player 0
            for i in range(0, self.size):                                                 #--------------------
                if i == action and action > 0:
                    action = state_list[i]
                    state_list[i] = 0
                    while(action != 0):
                        i+=1
                        if i == length - 2: i = 0
                        state_list[i] = state_list[i] + 1
                        action-=1                                                         #--------------------# logic for perfroming given action
                    if i == self.size:                                                    #--------------------# logic for perfroming special condition - where a player's last stone lands in their own mancala
                        state_list[-1] = 0
                    elif state_list[i] == 1 and i >= 0 and i < self.size:                 #--------------------# logic for perfroming special condition - where a player's last stone lands in one of their own empty cup
                        state_list[self.size] = state_list[self.size] + state_list[i] + state_list[(self.size*2)-i]
                        state_list[i] = 0
                        state_list[(self.size*2)-i] = 0
                        state_list[-1] = 1
                    else:
                        state_list[-1] = 1

        if state_list[-1] == 1:                                                           #logic for Player 1
            for i in range(self.size + 1, length - 2):                                    #--------------------
                if i == action and action > 0:
                    action = state_list[i]
                    state_list[i] = 0
                    while(action != 0):
                        i+=1
                        if i == self.size: i+=1
                        state_list[i] = state_list[i] + 1
                        if i == length - 2: i = -1
                        action-=1                                                   #--------------------# logic for perfroming given action
                    if i == -1:                                                   #--------------------# logic for perfroming special condition - where a player's last stone lands in their own mancala
                        state_list[-1] = 1
                    elif state_list[i] == 1 and i >= self.size + 1 and i < length - 2:    #--------------------# logic for perfroming special condition - where a player's last stone lands in one of their own empty cup
                        state_list[length-2] = state_list[length-2] + state_list[i] + state_list[(self.size*2)-i]
                        state_list[i] = 0
                        state_list[(self.size*2)-i] = 0
                        state_list[-1] = 0
                    else:
                        state_list[-1] = 0

        state = tuple(state_list)
        #print(state)
        return state
        #raise(Exception("Not implemented yet."))

    def is_over(self, state):
        """
        Return True if the game is over in the given state, False otherwise.
        The game is over if either player has no stones left in their small positions.
        """
        count_p0 = 0
        for i in range(0, self.size):
            if state[i] == 0:
                count_p0+=1
        count_p1 = 0
        for i in range(self.size + 1, len(state) - 2):
            if state[i] == 0:
                count_p1+=1
        if count_p0 == self.size or count_p1 == self.size:
            return True
        else:
            return False
        ## Finish me! ##
        #raise(Exception("Not implemented yet."))

    def score(self, state):
        """
        Return the score in the current state, from player 0's perspective.
        If the game is over and one player still has stones on their side,
        those stones are added to that player's score.
        """
        length = len(state)
        #print(state)
        player0_score = state[self.size]
        player1_score = state[length - 2]
        total_score = 0
        if self.is_over(state) == True:
            for i in range(0, self.size):               #calculating score if player 0 still has stones on its side
                player0_score+=state[i]
            for i in range(self.size + 1, length - 2):  #calculating score if player 1 still has stones on its side
                player1_score+=state[i]
            if state[-1] == 0:
                total_score = player0_score - player1_score
            else:
                total_score = player1_score - player0_score
        elif self.is_over(state) == False:
            if state[-1] == 0:
                total_score = ((state[self.size]) - (state[length - 2]))
            else:
                total_score = ((state[length - 2]) - (state[self.size]))
        #print(total_score)
        return total_score
        ## Finish me! ##
        #raise(Exception("Not implemented yet."))

    def string(self, state):
        """
        Display current state as a game board.  The current player's mancala
        is marked with *.
        """
        z = self.size
        s = " ".join(["%2d"%m for m in state[-2:z:-1]] + [" *" if state[-1]==0 else "  "])
        s += "\n"
        s += " ".join(["  " if state[-1]==0 else " *"] + ["%2d"%m for m in state[:(z+1)]])
        return s

if __name__ == "__main__":

    """
    Scratch pad for informal tests
    """

    mg = MancalaGame(size=6, count=4)
    s = mg.initial()
    state = (5, 5, 1, 1, 0, 6, 2, 6, 1, 1, 5, 1, 0, 2, 1)
    resstate = (0, 5, 1, 1, 0, 6, 2, 6, 1, 1, 5, 0, 0, 8, 0)
    s = mg.result(state,11)
    print(s)
    print(" ")
    print(resstate)
    exit(0)
    a = mg.actions(s)
    print(s)
    s = mg.result(s, 2)
    print(s)
    s = mg.result(s, 2)
    print(s)
    s = mg.result(s, 3)
    print(s)
    print("Is over: %s"%mg.is_over(s))
    print("Score = %d"%mg.score(s))
    s = mg.result(s, 3)
    print(s)
    s = mg.result(s, 4)
    print(s)
    s = mg.result(s, 5)
    print(s)
    s = mg.result(s, 2)
    print(s)
    print("Is over: %s"%mg.is_over(s))
    print("Score = %d"%mg.score(s))
    s = mg.result(s, 3)
    print(s)
    s = mg.result(s, 2)
    print(s)
    print("Is over: %s"%mg.is_over(s))
    print("Score = %d"%mg.score(s))
    s = mg.result(s, 2)
    print(s)
    print("Is over: %s"%mg.is_over(s))
    print("Score = %d"%mg.score(s))
    '''print(mg.string(s))
    print(s)
    print(a)
    print("Is over: %s"%mg.is_over(s))
    print("Score = %d"%mg.score(s))
    print("")

    s = mg.result(s, 2)
    a = mg.actions(s)
    print(mg.string(s))
    print(s)
    print(a)
    print("Is over: %s"%mg.is_over(s))
    print("Score = %d"%mg.score(s))
    print("")'''
