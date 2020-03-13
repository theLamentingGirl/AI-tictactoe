# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 05:06:07 2020

@author: gaGzy
"""

from tkinter import *
import numpy as np

class TicTacToe:
    
    #CLASS ATTRIB---------------------------
    
    #initializing game area
    #The game area is a 3x3 empty matrix filled with nan.

    #CLASS METHODS-----------------------
    #instance attributes are the values player1 or player 2 can give
    def __init__(self):
        self.p1=0
        self.p2=1
        self.draw=False
        self.gameArea=np.empty((3,3))
        self.gameArea.fill(None)
        self.buttonVal={"button1":'00',"button2":'01',"button3":'02',"button4":'10',\
                   "button5":'11',"button6":'12',"button7":'20',"button8":'21',\
                   "button9":'22'}
        self.pos=None
        self.inputChoices=['00','01','02','10','11','12','20','21','22']
        self.biasChoices=['11']

    def screen(self):
        
        '''goes through either rows or colums or diagonals to see if win'''
        for j in range(0,3):
            if self.gameArea[j,0] == self.gameArea[j,1] and self.gameArea[j,1] == self.gameArea[j,2]:
                if self.gameArea[j,1]==0:
                    return [True,"0"]
                else:
                    return[True,"1"]

        for j in range(0,3):
            if self.gameArea[0,j] == self.gameArea[2,j] and self.gameArea[1,j] == self.gameArea[2,j]:
                if self.gameArea[2,j]==0:
                    return [True,"0"]
                else:
                    return[True,"1"]
            
            
        if self.gameArea[0,0] == self.gameArea[2,2] and self.gameArea[1,1] == self.gameArea[0,0]:
                if self.gameArea[0,0]==0:
                    return [True,"0"]
                else:
                    return[True,"1"]

            
        if self.gameArea[2,0] == self.gameArea[1,1] and self.gameArea[2,0] == self.gameArea[0,2]:
                if self.gameArea[2,0]==0:
                    return [True,"0"]
                else:
                    return[True,"1"]
        return [False,"Draw"]    

    def checkWin(self):
        '''checks if the game is won by 8cases anyone or DRAW'''
        decision=self.screen()
#        print(decision)
        if decision[0] ==True:
#            print(decision[1], "won the game")
            return [True,int(decision[1])]
        
        else:
            if np.isnan(self.gameArea).any() == False:
                #GAME IS DRAW 
                self.draw=True
#                print("the Game is draw")
                return [True,'2']

        return [False,'']
#============================================================================

class playTicTacToe(TicTacToe):
#     
#    def __init__(self):
#        super().__init__()

    def __init__(self,*args): #OVERlOADED CONSTRUCTOR 
        super().__init__()
        if len(args)>0:
            self.gameArea=args[0]
#        else:
#            TicTacToe.gameArea
            

    def play(self):
        ''' Loop iterates until game is won/loss/draw
        else keep playing'''
        player=0
        winStatus=self.checkWin()
#        while self.prompt(player)==True:
        while not(winStatus[0]):
            print("the win condition is ",self.checkWin())
#            didhe=playerInterface().clickButton(whichbutton=None,buttonname=None)
            didhe=self.prompt(player)
            print('if he made a valid move:',didhe)
            if didhe==True:
                player=int(not(player))
#                if self.checkWin()==True:
        print(self.gameArea)
#                    
#            player=not(player)
#            print(int(player))
                
    def prompt(self,player,inputval=None):#new modified to take clicks as well
        '''Asks for a position'''
        if player==0:
            playerValue=self.p1
        else :
            playerValue=self.p2
            
#        buttonValue=self.buttonVal
#       pos=
        if inputval==None :
            self.pos=input(str("{} make a move:".format(int(player)))) #enter 33
#        print(pos,type(pos))
            if(len(self.pos)>2):
                print("enter valid position")
                return False
        else:
            self.pos=inputval
        
#        print("This is the value:",self.gameArea[int(pos[0]),int(pos[1])],"This is the type of gameArea val:",type(self.gameArea[int(pos[0]),int(pos[1])]))
        if np.isnan(self.gameArea[int(self.pos[0]),int(self.pos[1])]): 
            self.gameArea[int(self.pos[0]),int(self.pos[1])]=playerValue
#            print('entering values into',pos)
            return True
#        elif self.gameArea[int(pos[0]),int(pos[1])] == 1 or self.gameArea[int(pos[0]),int(pos[1])]==0:
        elif self.gameArea[int(self.pos[0]),int(self.pos[1])] == 1 or self.gameArea[int(self.pos[0]),int(self.pos[1])]==0:
            print('Error:the area is filled already')
            return False