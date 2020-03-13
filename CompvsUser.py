# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 15:06:59 2020

@author: gaGzy
"""
from PlayerInterFace import *
from RandomTicTacToe import *

class SinglePlay(playerInterface,RandomTicTacToe):
    def __init__(self):
        super().__init__()
        self.userStartButton.configure(command=self.playerClick)
        self.compStartButton.configure(command=self.compClick)

        self.buttonIndex={'00':self.button1,'01':self.button2,'02':self.button3,'10':self.button4,\
                          '11':self.button5,'12':self.button6,'20':self.button7,'21':self.button8,\
                          '22':self.button9}
        self.parent.mainloop()
        
    def playerClick(self):
        print("This is inside player click" )
        self.compStartButton.configure(state=DISABLED)
        self.userStartButton.configure(state=DISABLED)

        self.button1.configure(command=lambda:self.playerPlay(self.button1,"button1"))
        self.button2.configure(command=lambda:self.playerPlay(self.button2,"button2"))
        self.button3.configure(command=lambda:self.playerPlay(self.button3,"button3"))
        self.button4.configure(command=lambda:self.playerPlay(self.button4,"button4"))
        self.button5.configure(command=lambda:self.playerPlay(self.button5,"button5"))
        self.button6.configure(command=lambda:self.playerPlay(self.button6,"button6"))
        self.button7.configure(command=lambda:self.playerPlay(self.button7,"button7"))
        self.button8.configure(command=lambda:self.playerPlay(self.button8,"button8"))
        self.button9.configure(command=lambda:self.playerPlay(self.button9,"button9"))

        #1st player plays then comp
    def compClick(self):
        print("This is inside comp click" )
        self.compStartButton.configure(state=DISABLED)
        self.userStartButton.configure(state=DISABLED)

        self.button1.configure(command=lambda:self.compPlay(self.button1,"button1"))
        self.button2.configure(command=lambda:self.compPlay(self.button2,"button2"))
        self.button3.configure(command=lambda:self.compPlay(self.button3,"button3"))
        self.button4.configure(command=lambda:self.compPlay(self.button4,"button4"))
        self.button5.configure(command=lambda:self.compPlay(self.button5,"button5"))
        self.button6.configure(command=lambda:self.compPlay(self.button6,"button6"))
        self.button7.configure(command=lambda:self.compPlay(self.button7,"button7"))
        self.button8.configure(command=lambda:self.compPlay(self.button8,"button8"))
        self.button9.configure(command=lambda:self.compPlay(self.button9,"button9"))
    
        
        #1st comp plays then player
    def playerPlay(self,whichbutton,buttonname):
        
        print("This is user move")
#        player=self.player
        winStatus=self.checkWin()

#        while self.prompt(player)==True:
        if not(winStatus[0]):

            print("the win condition is ",self.checkWin())
#            didhe=playerInterface().clickButton(whichbutton=None,buttonname=None)
            if self.player==0:
                textToPut='O'
            else:
                textToPut='X'

            didhe=self.prompt(self.player,self.buttonVal[buttonname])
            self.playerBox.configure(text=textToPut)
            print("This is didhe",didhe)
            self.winner()
            print("This is player",self.player)
            if didhe==True:
                self.player=int(not(self.player))

            whichbutton["text"]=textToPut
            whichbutton.configure(state=DISABLED)
#            print(whichbutton,type(whichbutton))
            self.inputChoices.remove(self.pos)


        print(self.gameArea)
#        print("This is input choices",self.inputChoices)
            # WHO PLAYS FIRST 
        winStatus=self.checkWin()
#        print('the win status: ', winStatus)
#        ''' Loop iterates until game is won/loss/draw
#        else keep playing'''
        print("This is comp move")
#        player=self.player

        bias=1
        if not(winStatus[0]):

            print("the win condition is ",self.checkWin())
            if self.player==0:
                textToPut='O'
            else:
                textToPut='X'

            didhe=self.prompt(self.player,self.choose())
            bias=0
            print('if he made a valid move:',didhe)
            self.winner()
#            print("This is player",self.player)
            if didhe==True:
                self.player=int(not(self.player))
            winStatus=self.checkWin()
        pos=self.pos[0]+self.pos[1]
        
        #---Here the code fucks up. whichbutton is a str. Fix it
        whichbutton=self.buttonIndex[pos]
        whichbutton.configure(text=textToPut)
        whichbutton.configure(state=DISABLED)

        print(self.gameArea)
        print(self.inputChoices)
#        return winStatus[1]

    def compPlay(self,whichbutton,buttonname):
            # WHO PLAYS FIRST 
        winStatus=self.checkWin()
#        print('the win status: ', winStatus)
#        ''' Loop iterates until game is won/loss/draw
#        else keep playing'''
        print("This is comp move")
#        player=self.player

        bias=1
        if not(winStatus[0]):

            print("the win condition is ",self.checkWin())
            if self.player==0:
                textToPut='O'
            else:
                textToPut='X'

            didhe=self.prompt(self.player,self.choose())
            print(self.choose())
            pos=self.pos[0]+self.pos[1]
            bias=0
            print('if he made a valid move:',didhe)
            self.winner()
#            print("This is player",self.player)
            if didhe==True:
                self.player=int(not(self.player))
            winStatus=self.checkWin()
            
        
        #---Here the code fucks up. whichbutton is a str. Fix it
        whichbutton=self.buttonIndex[pos]
        whichbutton.configure(text=textToPut)
        whichbutton.configure(state=DISABLED)

        print(self.gameArea)
        print(self.inputChoices)
#        return winStatus[1]
#         return winStatus[1]
        print("This is user move")
#        player=self.player
        winStatus=self.checkWin()

#        while self.prompt(player)==True:
        if not(winStatus[0]):

            print("the win condition is ",self.checkWin())
#            didhe=playerInterface().clickButton(whichbutton=None,buttonname=None)
            if self.player==0:
                textToPut='O'
            else:
                textToPut='X'

            didhe=self.prompt(self.player,self.buttonVal[buttonname])
            self.playerBox.configure(text=textToPut)
            print("This is didhe",didhe)
            self.winner()
            print("This is player",self.player)
            if didhe==True:
                self.player=int(not(self.player))

            whichbutton["text"]=textToPut
            whichbutton.configure(state=DISABLED)
#            print(whichbutton,type(whichbutton))
            self.inputChoices.remove(self.pos)


        print(self.gameArea)

def main():
    SinglePlay()
    
if __name__=="__main__":main()