from PlayerInterFace import *
from RandomTicTacToe import *
import numpy as np
from sys import maxsize

class MinMax(playerInterface, RandomTicTacToe):
    def __init__(self):
        super().__init__()
    # just assigned emoty to be assigned later
        self.scores = np.nan
        self.buttonIndex = {'00': self.button1, '01': self.button2, '02': self.button3, '10': self.button4,
                        '11': self.button5, '12': self.button6, '20': self.button7, '21': self.button8,
                        '22': self.button9}
#        self.maximiser=''
#        self.minimiser=''

    def bestMove(self):
        # score of maximising player is positive->10;
        # score of minimising player is negative->-10;
        # score of draw->0
        if self.player == 0:
            self.scores = {"0": "10", "1": "-10", "2": "0"}
#            self.maximiser=0
#            self.minimiser=1
        else:
            self.scores = {"0": "-10", "1": "10", "2": "0"}
#            self.maximiser=1
#            self.minimiser=0
    #        print("these are my scores",self.scores)
        '''initialising the bestScore to be -infinity since that's the smallest number,
        we wish to find a bestScore that's definitely greater than smallest number'''
        bestScore = -maxsize
    #       print("this is the player",self.player)
    # 2 for loops to sweep through the gameArea
        for i in range(3):
            for j in range(3):
                #                print('printing from bestmove',type(self.gameArea))
                #                print("This is player call from bestmove",self.player)
                # bestPos returns the best position after running the minmax algorithm
                if np.isnan(self.gameArea[i, j]):  # if its empty
                    self.gameArea[i, j] = self.player  # temp assignment
                    score = self.algorithm(self.gameArea, 0, False)
                    # needed to empty that spot so that real bestPos can be feeded
                    self.gameArea[i, j] = np.nan
                    if int(score) > int(bestScore):
                        bestScore = score
                        bestPos = str(i)+str(j)
        return bestPos

    def algorithm(self, gameArea, depth, isMax):
        # First checks the win condition
        checkWin = self.checkWin()
        result = checkWin[0]
        whoWon = checkWin[1]
        # to break the recursive fn
        if result == True:
            #            print("condition of algo is true and whoWon",whoWon)
            #           print(self.scores[str(whoWon)])
            return self.scores[str(whoWon)]
#            if self.maximiser==0 and whoWon==self.maximiser:#0->
#                print("inside cond1")
#                self.scores[str(whoWon)]=int(self.scores[str(whoWon)])-depth
#                return self.scores[str(whoWon)]
##                print(self.scores[str(whoWon)])
#            elif self.minimiser==1 and whoWon==self.minimiser:
#                print("inside cond2")
#                self.scores[str(whoWon)]=int(self.scores[str(whoWon)])+depth
#                return self.scores[str(whoWon)]
##                print(self.scores[str(whoWon)])
#            elif self.maximiser==1 and whoWon==self.maximiser:
#                print("inside cond3")
#                self.scores[str(whoWon)]=int(self.scores[str(whoWon)])+depth
#                return self.scores[str(whoWon)]
#            elif self.minimiser==0 and whoWon==self.minimiser:
#                print("inside cond4")
#                self.scores[str(whoWon)]=int(self.scores[str(whoWon)])-depth
#                return self.scores[str(whoWon)]
    
        # if it's the maximising players turn
        elif isMax == True:
            bestScore = -maxsize
    #            print("This is the max player",self.player)
    # 2 for loops create one full instance gameState
            for i in range(3):
                for j in range(3):
                    if np.isnan(gameArea[i, j]):
                        #                        print(self.player)
                        gameArea[i, j] = self.player  # 1
                        score = self.algorithm(gameArea, depth+1, False)
                        gameArea[i, j] = np.nan
                        bestScore = max(int(score), int(bestScore))
            return bestScore
    
        else:  # False if it's the minimising player's turn
            bestScore = maxsize
    #            print("This is the min player",self.player)
            for i in range(3):
                for j in range(3):
                    if np.isnan(gameArea[i, j]):
                        #                        print(self.player)
                        #                        self.player=not(self.player)
                        gameArea[i, j] = not(self.player)  # 0
                        score = self.algorithm(gameArea, depth+1, True)
                        gameArea[i, j] = np.nan
                        bestScore = min(int(score), int(bestScore))
            return bestScore
    # -------------------------------------------------------------------------------------------


class PlayGame(MinMax):
    def __init__(self):
        super().__init__()
#        print("just initted super, and my scoresare",self.scores)
        self.userStartButton.configure(command=self.playerClick)
        self.compStartButton.configure(command=self.compClick)

        self.parent.mainloop()

    def playerClick(self):
        # print command tells which click is activated
        print("This is inside player click")
        self.compStartButton.configure(state=DISABLED)
        self.userStartButton.configure(state=DISABLED)

        # assigning button fns
        self.button1.configure(
            command=lambda: self.playerPlay(self.button1, "button1"))
        self.button2.configure(
            command=lambda: self.playerPlay(self.button2, "button2"))
        self.button3.configure(
            command=lambda: self.playerPlay(self.button3, "button3"))
        self.button4.configure(
            command=lambda: self.playerPlay(self.button4, "button4"))
        self.button5.configure(
            command=lambda: self.playerPlay(self.button5, "button5"))
        self.button6.configure(
            command=lambda: self.playerPlay(self.button6, "button6"))
        self.button7.configure(
            command=lambda: self.playerPlay(self.button7, "button7"))
        self.button8.configure(
            command=lambda: self.playerPlay(self.button8, "button8"))
        self.button9.configure(
            command=lambda: self.playerPlay(self.button9, "button9"))

        # 1st player plays then comp
    def compClick(self):
        # print command tells which click activated
        print("This is inside comp click")
        # disabling buttons
        self.compStartButton.configure(state=DISABLED)
        self.userStartButton.configure(state=DISABLED)
#        self.player=1
        winStatus = self.checkWin()

        # if cond.- checking win status
        if not(winStatus[0]):
            # print-whose move
            print("This is comp move")
            # print-winCond.
            print("the win condition is ", self.checkWin())

            # assigning 'X'to 1 and 'O' to 0
            if self.player == 0:
                textToPut = 'O'
            else:
                textToPut = 'X'

            # assigning the prompt fn to didhe object
            # prompt sets the value of X or O as 0 or 1 in the gameArea
            print(self.player)
            # changes from CompvsUser
            didhe = self.prompt(self.player, self.choose())#initial value choosen by comp is random

            print(self.gameArea)

            print('if he made a valid move:', didhe)
            # winner-checks win cond. and tells who wins in the playerBox/tells if draw
            self.winner()

    #            winStatus=self.checkWin()
            # assigning the X or O in the playerInterface
            pos = self.pos[0]+self.pos[1]

            whichbutton = self.buttonIndex[pos]
            whichbutton.configure(text=textToPut)
            whichbutton.configure(state=DISABLED)

            # changing the player if the winCond is true
            if didhe == True:
                self.player = int(not(self.player))

        self.button1.configure(
            command=lambda: self.playerPlay(self.button1, "button1"))
        self.button2.configure(
            command=lambda: self.playerPlay(self.button2, "button2"))
        self.button3.configure(
            command=lambda: self.playerPlay(self.button3, "button3"))
        self.button4.configure(
            command=lambda: self.playerPlay(self.button4, "button4"))
        self.button5.configure(
            command=lambda: self.playerPlay(self.button5, "button5"))
        self.button6.configure(
            command=lambda: self.playerPlay(self.button6, "button6"))
        self.button7.configure(
            command=lambda: self.playerPlay(self.button7, "button7"))
        self.button8.configure(
            command=lambda: self.playerPlay(self.button8, "button8"))
        self.button9.configure(
            command=lambda: self.playerPlay(self.button9, "button9"))
        self.playerBox.configure(text='X')

    def playerPlay(self, whichbutton, buttonname):

        winStatus = self.checkWin()

        if winStatus[0] == False:
            print("This is user move")
            print("the win condition is ", self.checkWin())

            # assigning the X and O to 1 and 0 resp.
            if self.player == 0:
                textToPut = 'O'
            else:
                textToPut = 'X'

            # prompt-enters values into gameArea
            didhe = self.prompt(self.player, self.buttonVal[buttonname])
            # updates player interface
            whichbutton["text"] = textToPut
            whichbutton.configure(state=DISABLED)

           # now checks if the win cond is true
            winStatus = self.checkWin()
            # if win cond. true
            if winStatus[0] == True:
                self.winner()
                self.playerBox.configure(text=textToPut)
            # win cond. false->comp move after changing the player
            else:
                print("Did he makea valid move", didhe)
    #               print("This is player who played",self.player)
                # checks validmove and changes player
                if didhe == True:
                    self.player = int(not(self.player))
                # assigns X or O in the playerInterface
                self.playerBox.configure(text=textToPut)
                print(self.gameArea)
    # ------------------------------------------------------------------------------
                print("This is comp move")
                print("the win condition is ", self.checkWin())
                # assigns X and O
                if self.player == 0:
                    textToPut = 'O'
                else:
                    textToPut = 'X'
                # comp chooses a best value throgh the minmax class bestmove and fills game area

                print("This is the comp player in playerplay", self.player)
                didhe = self.prompt(self.player, self.bestMove())
                print("this is the best position", self.pos)
                pos = self.pos[0]+self.pos[1]
                whichbutton = self.buttonIndex[pos]
                whichbutton.configure(text=textToPut)
                whichbutton.configure(state=DISABLED)

                print(self.gameArea)

                # now check if win cond is true/false
                winStatus = self.checkWin()
                # if win cond is true
                if winStatus[0] == True:
                    self.winner()
                    self.playerBox.configure(text=textToPut)
                # if win cond is false: CHANGE PLAYERBOX
                else:
                    print('if he made a valid move:', didhe)
                    if didhe == True:
                        self.player = int(not(self.player))

                    if self.player == 0:
                        textToPut = 'O'
                    else:
                        textToPut = 'X'
                    # value in player box
                    self.playerBox.configure(text=textToPut)


def main():
    PlayGame()


if __name__ == "__main__":
    main()
