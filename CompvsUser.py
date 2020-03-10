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

        self.buttonIndex={'00':"button1",'01':"button2",'02':"button3",'10':"button4",\
                          '11':"button5",'12':"button6",'20':"button7",'21':"button8",\
                          '22':"button9"}
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
        player=self.player
        winStatus=self.checkWin()
#        while self.prompt(player)==True:
        if not(winStatus[0]):
            print("the win condition is ",self.checkWin())
#            didhe=playerInterface().clickButton(whichbutton=None,buttonname=None)
            if player==0:
                textToPut='O'
            else:
                textToPut='X'

            didhe=self.prompt(player,self.buttonVal[buttonname])
            self.playerBox.configure(text=textToPut)

            whichbutton["text"]=textToPut
            whichbutton.configure(state=DISABLED)
            self.inputChoices.remove(self.pos)
        self.winner()
        print(self.gameArea)
        print("This is input choices",self.inputChoices)
            # WHO PLAYS FIRST 
#        winStatus=self.checkWin()
#        print('the win status: ', winStatus)
#        ''' Loop iterates until game is won/loss/draw
#        else keep playing'''
        print("This is comp move")
        player=self.player
        bias=1
        if not(winStatus[0]):
            if player==0:
                textToPut='O'
            else:
                textToPut='X'

            print("the win condition is ",self.checkWin())
            didhe=self.prompt(player,self.choose())
            bias=0
            print('if he made a valid move:',didhe)
            if didhe==True:
                player=int(not(player))
            winStatus=self.checkWin()
        pos=self.pos[0]+self.pos[1]
        
        #---Here the code fucks up. whichbutton is a str. Fix it
        self.whichbutton=self.buttonIndex[pos]
        self.whichbutton.configure(text=textToPut)
        self.whichbutton.configure(state=DISABLED)
        self.winner()
        print(self.gameArea)
#        return winStatus[1]

    def compPlay(self,whichbutton,buttonname):
        winStatus=self.checkWin()
        player=self.player
        bias=1
        if not(winStatus[0]):
            
            if player==0:
                textToPut='O'
            else:
                textToPut='X'

            print("the win condition is ",self.checkWin())
            didhe=self.prompt(player,self.choose())
            bias=0
            print('if he made a valid move:',didhe)
            if didhe==True:
                player=int(not(player))
            winStatus=self.checkWin()
        pos=self.pos[0]+self.pos[1]
        whichbutton=self.buttonIndex[pos]
        self.whichbutton["text"]=textToPut
        self.whichbutton.configure(state=DISABLED)
        self.winner()
        
        
        player=self.player
        winStatus=self.checkWin()
#        while self.prompt(player)==True:
        if not(winStatus[0]):
            print("the win condition is ",self.checkWin())
#            didhe=playerInterface().clickButton(whichbutton=None,buttonname=None)
            if player==0:
                textToPut='O'
            else:
                textToPut='X'
                
            didhe=self.prompt(player,self.buttonVal[buttonname])
            self.playerBox.configure(text=textToPut)
            whichbutton["text"]=textToPut
            whichbutton.configure(state=DISABLED)
            self.inputChoices.remove(self.pos)
        self.winner()
        
            
            
def main():
    SinglePlay()
    
if __name__=="__main__":main()