"""
Created on Tue Mar 10 15:06:59 2020

@author: gaGzy
"""
'''ALL BUGS FIXED'''




from PlayerInterFace import *
from RandomTicTacToe import *
class SinglePlay(playerInterface, RandomTicTacToe):
    def __init__(self):
        super().__init__()
        self.userStartButton.configure(command=self.playerClick)
        self.compStartButton.configure(command=self.compClick)

        self.buttonIndex = {'00': self.button1, '01': self.button2, '02': self.button3, '10': self.button4,
                            '11': self.button5, '12': self.button6, '20': self.button7, '21': self.button8,
                            '22': self.button9}
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
            didhe = self.prompt(self.player, self.choose())

            print(self.gameArea)
            print(self.inputChoices)
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
            # removes the choices from whch comp can choose
            self.inputChoices.remove(self.pos)

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
                print(self.inputChoices)
# ------------------------------------------------------------------------------
                print("This is comp move")
                print("the win condition is ", self.checkWin())
                # assigns X and O
                if self.player == 0:
                    textToPut = 'O'
                else:
                    textToPut = 'X'
                # comp chooses a random value throgh the function choose and fills game area
                didhe = self.prompt(self.player, self.choose())

                pos = self.pos[0]+self.pos[1]
                whichbutton = self.buttonIndex[pos]
                whichbutton.configure(text=textToPut)
                whichbutton.configure(state=DISABLED)

                print(self.gameArea)
                print(self.inputChoices)

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
    SinglePlay()


if __name__ == "__main__":
    main()
