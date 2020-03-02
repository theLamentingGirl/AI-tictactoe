# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 16:54:12 2020

@author: gaGzy
"""

import numpy as np

class TicTacToe:
    #CLASS ATTRIB---------------------------
    
    #initializing game area
    #The game area is a 3x3 empty matrix filled with nan.
    gameArea=np.empty((3,3))
    gameArea.fill(np.nan)
    
    #CLASS METHODS-----------------------
    #instance attributes are the values player1 or player 2 can give
    def __init__(self):
        self.p1=0
        self.p2=1
        self.draw=False
    
#    def validMove(self):

#    def checkGameStatus(self):

    def screen(self):
        
        '''goes through either rows or colums or diagonals to see if win'''
        for j in range(0,3):
            if self.gameArea[j,0] == self.gameArea[j,1] and self.gameArea[j,1] == self.gameArea[j,2]:
                if self.gameArea[j,1]==0:
                    return [True,"p1"]
                else:
                    return[True,"p2"]

        for j in range(0,3):
            if self.gameArea[0,j] == self.gameArea[2,j] and self.gameArea[1,j] == self.gameArea[2,j]:
                if self.gameArea[2,j]==0:
                    return [True,"p1"]
                else:
                    return[True,"p2"]
            
            
        if self.gameArea[0,0] == self.gameArea[2,2] and self.gameArea[1,1] == self.gameArea[0,0]:
                if self.gameArea[0,0]==0:
                    return [True,"p1"]
                else:
                    return[True,"p2"]

            
        if self.gameArea[2,0] == self.gameArea[1,1] and self.gameArea[2,0] == self.gameArea[0,2]:
                if self.gameArea[2,0]==0:
                    return [True,"p1"]
                else:
                    return[True,"p2"]
        return False    
            
    def checkWin(self):
        '''checks if the game is won by 8cases anyone or DRAW'''
        decision=self.screen()
        print(decision)
        if decision[0] ==True:
            return True
        else:
            if np.isnan(self.gameArea).any() == False:
                #GAME IS DRAW 
                self.draw=True
                return True
#    def whoWon(self):
#        '''output whether p1 or p2 won'''
#        if 
#============================================================================

class playTicTacToe(TicTacToe):
     
    def __init__(self):
        super().__init__()

    def __init__(self,state): #OVERlOADED CONSTRUCTOR 
        super().__init__()
        TicTacToe.gameArea=state

    def play(self):
        ''' Loop iterates until game is won/loss/draw
        else keep playing'''
        player=0
        while not(self.checkWin()):
            didhe=self.prompt(player)
            if didhe==True:
                player=int(not(player))
                
    def prompt(self,player):
        '''Asks for a position'''
        if player==0:
            playerValue=self.p1
        else :
            playerValue=self.p2
        
        pos=input("{} make a move:".format(player)) #enter 33
        if(len(pos)>2):
            print("enter valid position")
            return False
        
        if self.gameArea[pos[0],pos[1]] is None:
            self.gameArea[pos[0],pos[1]]=playerValue
            return True
        else :
            print('Error:the area is filled already')
            return False
#=============================================================================

#MAIN FUNCTION

def main():
    #HOW TO TEST THE GAME
    playState=np.array([[1,0,1],[0,1,0],[0,0,1]])
    playState2=np.array([[0,0,1],[0,1,0],[0,1,1]])
    playState3=np.array([[1,0,1],[0,1,0],[0,1,0]])
    
    
    testPlay=playTicTacToe(playState2) #obj created
#    if testPlay.draw==True:
#        print("Draw")
#    else:
    decision=testPlay.screen()
    if decision!=False:
        who=decision[1]
        print(who,' won the game')
    else:
        print("Draw")

if __name__=="main":
    main()

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
#    #Main fn to start playing
#    def playTickTackToe():
#        
#        return #print Player1 /Player2 wins 

#    #setting values one by one
#    def setValues(self):
#        dictVal=self.input
#        index=list(dictVal.keys())
#        values=list(dictVal.values())
#        
#        for i in range(len(values)):
#            ind=index[i]
#            row=ind[0]
#            col=ind[1]
#            
#            self.empty[row,col]=values[i]
#    
#            #checking if the values are valid
#            checkValidMove(self):
#                if values[i]=!1 or values[i]=!2:
#                    print("Invalid value")
#                if True:
#                    for j in len(index):
#                        
#                
#                
#            def returnValues(self):
#                
#            
#            def checkGameStage(self):
#                def checkWinStatus():
#            
    
    
        