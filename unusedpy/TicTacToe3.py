# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 14:11:34 2020

@author: gaGzy
"""
from tkinter import *
import numpy as np

class TicTacToe(GameArea):
    #CLASS ATTRIB---------------------------
    

    #CLASS METHODS-----------------------
    #instance attributes are the values player1 or player 2 can give
    def __init__(self):
        super().__init__()
        self.p1=0
        self.p2=1
#        self.draw=False

    def screen(self,player):
        if button1['text'] == player and button2['text'] == player and button3['text'] == player or \
            button4['text'] == player and button5['text'] == player and button6['text'] == player or \
            button7['text'] ==player and button8['text'] == player and button9['text'] == player or\
            button1['text'] == player and button5['text'] == player and button9['text'] == player or\
            button3['text'] == player and button5['text'] == player and button7['text'] == player or\
            button1['text'] == player and button2['text'] == player and button3['text'] == player or\
            button1['text'] == player and button4['text'] == player and button7['text'] == player or\
            button2['text'] == player and button5['text'] == player and button8['text'] == player or\
            button7['text'] == player and button6['text'] == player and button9['text'] == player:
            return [True,player]

        else:
            return [False,'']
         
    def disableAll(self):
        self.button1.configure(state=DISABLED)
        self.button2.configure(state=DISABLED)
        self.button3.configure(state=DISABLED)
        self.button4.configure(state=DISABLED)
        self.button5.configure(state=DISABLED)
        self.button6.configure(state=DISABLED)
        self.button7.configure(state=DISABLED)
        self.button8.configure(state=DISABLED)
        self.button9.configure(state=DISABLED)

    def checkWin(self,player):
        '''checks if the game is won by 8cases anyone or DRAW'''
        decision=self.screen()
#        print(decision)
        if decision[0] ==True:
            self.playerBox.configure(text=player)
            self.textBox.configure(text="won the game")
            return True
#        
#        else:
#            if np.isnan(self.gameArea).any() == False:
#                #GAME IS DRAW 
#                self.draw=True
#                print("the Game is draw")
#                return True
        return False
    +++++++
#============================================================================

class playTicTacToe(TicTacToe):

    def __init__(self,*args): 
        super().__init__()
        if len(args)>0:
            self.gameArea=args[0]

        self.gameArea=GameArea()

    def play(self):
        
        player=0
        self.gameArea.button1.configure(command=lambda:self.buttonClick(button1))
        self.gameArea.button2.configure(command=lambda:self.buttonClick(button2))
        self.gameArea.button3.configure(command=lambda:self.buttonClick(button3))
        self.gameArea.button4.configure(command=lambda:self.buttonClick(button4))
        self.gameArea.button5.configure(command=lambda:self.buttonClick(button5))
        self.gameArea.button6.configure(command=lambda:self.buttonClick(button6))
        self.gameArea.button7.configure(command=lambda:self.buttonClick(button7))
        self.gameArea.button8.configure(command=lambda:self.buttonClick(button8))
        self.gameArea.button9.configure(command=lambda:self.buttonClick(button9))
        ''' Loop iterates until game is won/loss/draw
        else keep playing'''
        
        while self.checkWin()==False:
            player=int(not(player))
        else:
            self.disableAll()
            
#        while not(self.checkWin()):
#            print("the win condition is ",self.checkWin())
#            didhe=self.prompt(player)
#            print('if he made a valid move:',didhe)
#            if didhe==True:
#                player=int(not(player))
#
#        print(self.gameArea)
#set the value
    def prompt(self,whichbutton):#,player):
        '''Asks for a position'''
        if player==0:
            playerValue=self.p1
        else:
            playerValue=self.p2
        self.gameArea.whichbutton.configure(text=playerValue,state=DISABLED)
        self.playerBox.configure(text=player)

    def buttonClick(self,whichbutton):
        if whichbutton['text']=='':
            self.prompt(whichbutton)

#        if np.isnan(self.gameArea[int(pos[0]),int(pos[1])]): #== self.gameAreaDummy[1,1].item() :
#            self.gameArea[int(pos[0]),int(pos[1])]=playerValue
##            print('entering values into',pos)
#            return True
##        elif self.gameArea[int(pos[0]),int(pos[1])] == 1 or self.gameArea[int(pos[0]),int(pos[1])]==0:
#        elif self.gameArea[int(pos[0]),int(pos[1])] == 1 or self.gameArea[int(pos[0]),int(pos[1])]==0:
#            print('Error:the area is filled already')
            return False

#=============================================================================

class GameArea():
    def __init__(self):
        self.parent=Tk()
    
    #partition1 for other buttons
        self.partition1=Frame(self.parent)
        self.partition1.pack(side=TOP)
        
        self.quitButton=Button(self.partition1,text="QUIT",padx=10,pady=2,command=root.destroy)
        self.quitButton.pack(side=RIGHT)

        self.playerBox=Label(self.partition1)
        self.playerBox.pack(side=RIGHT)

        self.textBox=Label(self.partition1,text="make a move")
        self.textBox.pack(side=RIGHT)
        
        self.resetButton=Button(self.partition1,text="RESET",padx=10,pady=2)
        self.resetButton.pack(side=RIGHT)

    #partition 2 for containing the tictactoe buttons
        
        self.partition2=Frame(self.parent)
        self.partition2.pack(side=TOP)
        
        #three frames for positioning the buttons
        self.topframe = Frame(self.partition2)
        self.topframe.pack(side=BOTTOM)
        
        self.midframe = Frame(self.partition2)
        self.midframe.pack(side=BOTTOM)
        
        self.bottomframe = Frame(self.partition2)
        self.bottomframe.pack( side = BOTTOM )
        
    #-----------BUTTONS---------------------------
        #button1
        self.button1=Button(self.topframe,padx=50,pady=50)
        self.button1.pack(side=LEFT)
        
        
        #button2
        self.button2=Button(self.topframe,padx=50,pady=50)
        self.button2.pack(side=LEFT)
        
        #button3
        self.button3=Button(self.topframe,padx=50,pady=50)
        self.button3.pack(side=LEFT)
        
        #button4
        self.button4=Button(self.midframe,padx=50,pady=50)
        self.button4.pack(side=LEFT)
        
        #button5
        self.button5=Button(self.midframe,padx=50,pady=50)
        self.button5.pack(side=LEFT)
        
        #button6
        self.button6=Button(self.midframe,padx=50,pady=50)
        self.button6.pack(side=LEFT)
        
        #button7
        self.button7=Button(self.bottomframe,padx=50,pady=50)
        self.button7.pack(side=LEFT)
        
        #button8
        self.button8=Button(self.bottomframe,padx=50,pady=50)
        self.button8.pack(side=LEFT)
        
        #button9
        self.button9=Button(self.bottomframe,padx=50,pady=50)
        self.button9.pack(side=LEFT)
        
        self.parent.mainloop()

def main():

    testGame=playTicTacToe()
    testGame.play()
    

if __name__=="main": main()
