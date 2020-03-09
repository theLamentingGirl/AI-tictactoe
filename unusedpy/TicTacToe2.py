# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 04:11:33 2020

@author: gaGzy
"""

import numpy as np

class TicTacToe:
    #CLASS ATTRIB---------------------------
    
    #initializing game area
    #The game area is a 3x3 empty matrix filled with nan.

#    gameArea=np.empty((3,3))
#    gameArea.fill(None)
#    print(gameArea)
    
    

    #CLASS METHODS-----------------------
    #instance attributes are the values player1 or player 2 can give
    def __init__(self):
        self.p1=0
        self.p2=1
        self.draw=False
        self.gameArea=np.empty((3,3))
        self.gameArea.fill(None)
#        print(self.gameArea)
        
        
    
    
#    def validMove(self):

#    def checkGameStatus(self):

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
#        for j in range(0,3):
#            if self.gameArea[j,0] == self.gameArea[j,1] and self.gameArea[j,1] == self.gameArea[j,2]:
#                return True
#        for j in range(0,3):
#            if self.gameArea[0,j] == self.gameArea[2,j] and self.gameArea[1,j] == self.gameArea[2,j]:
#                return True
#        if self.gameArea[0,0] == self.gameArea[2,2] and self.gameArea[1,1] == self.gameArea[0,0]:
#                return True
#        if self.gameArea[2,0] == self.gameArea[1,1] and self.gameArea[2,0] == self.gameArea[0,2]:
#                return True
#                
#        return False    
            
    def checkWin(self):
        '''checks if the game is won by 8cases anyone or DRAW'''
        decision=self.screen()
#        print(decision)
        if decision[0] ==True:
            print(decision[1], "won the game")
            return True
        
        else:
            if np.isnan(self.gameArea).any() == False:
                #GAME IS DRAW 
                self.draw=True
                print("the Game is draw")
                return True
#        if self.screen() ==True:
#            return True
#        else:
#            if np.isnan(self.gameArea).any() == False:
#                #GAME IS DRAW 
#                self.draw=True
#                return True
        return False
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
                
#        while self.prompt(player)==True:
        while not(self.checkWin()):
            print("the win condition is ",self.checkWin())
            didhe=self.prompt(player)
            print('if he made a valid move:',didhe)
            if didhe==True:
                player=int(not(player))
#                if self.checkWin()==True:
        print(self.gameArea)
#                    
#            player=not(player)
#            print(int(player))
                
    def prompt(self,player):
        '''Asks for a position'''
        if player==0:
            playerValue=self.p1
        else :
            playerValue=self.p2
        pos=input(str("{} make a move:".format(int(player)))) #enter 33
#        print(pos,type(pos))
#        if(len(pos)>2):
#            print("enter valid position")
#            return False
#        print("This is the value:",self.gameArea[int(pos[0]),int(pos[1])],"This is the type of gameArea val:",type(self.gameArea[int(pos[0]),int(pos[1])]))
        if np.isnan(self.gameArea[int(pos[0]),int(pos[1])]): #== self.gameAreaDummy[1,1].item() :
            self.gameArea[int(pos[0]),int(pos[1])]=playerValue
#            print('entering values into',pos)
            return True
#        elif self.gameArea[int(pos[0]),int(pos[1])] == 1 or self.gameArea[int(pos[0]),int(pos[1])]==0:
        elif self.gameArea[int(pos[0]),int(pos[1])] == 1 or self.gameArea[int(pos[0]),int(pos[1])]==0:
            print('Error:the area is filled already')
            return False

#=============================================================================

#MAIN FUNCTION

def main():
    
#    playState=np.array([[1,0,1],[0,1,0],[0,0,1]])
#    playState2=np.array([[0,0,1],[0,1,0],[0,1,1]])
#    playState3=np.array([[1,0,1],[0,1,0],[0,1,0]])
#    testPlay=playTicTacToe(playState)
#    testPlay.play()
    
    
    #HOW TO TEST THE GAME for player1 and player 2





    PlayerGame=playTicTacToe()
    PlayerGame.play()
#    
#    decision=PlayerGame.screen()
#    if decision[0]!=False:
#        who=decision[1]
#        print(who,' won the game')
#    else:
#        print("Draw")
    
#    print(who,' won the game')
#    print(testPlay.draw)

if __name__=="main": main()
