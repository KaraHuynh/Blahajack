class Turn:

    def __init__(self, turn):
        self.p_turn = turn

    def nextTurn(self):
        if(self.p_turn == 1):
            self.p_turn = 2
            print("Player 2's turn")
        elif(self.p_turn == 2):
            self.p_turn = 1
            print("Player 1's turn")
        else:
            print("wtf")