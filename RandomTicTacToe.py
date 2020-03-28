# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 03:30:49 2020

@author: gaGzy
"""
from GameEngine import *
import random

class RandomTicTacToe(playTicTacToe):
    playNo=1000
    def __init__(self):
        super().__init__()
        self.inputChoices=['00','01','02','10','11','12','20','21','22']
        self.biasChoices=['00','02','20','22']
#        '00','02','20','22'

    def randomPlay(self):
        player=0  # WHO PLAYS FIRST 
        winStatus=self.checkWin()
#        print('the win status: ', winStatus)
        ''' Loop iterates until game is won/loss/draw
        else keep playing'''
        bias=1
        while not(winStatus[0]):
#            print("the win condition is ",self.checkWin())
            didhe=self.prompt(player,self.biasChoose(bias))
            bias=0
#            print('if he made a valid move:',didhe)
            if didhe==True:
                player=int(not(player))
            winStatus=self.checkWin()

#        print(self.gameArea)
        return winStatus[1]
    
    def biasChoose(self,switch=1):
        if switch==1:
            choice=random.choice(self.biasChoices)
        else :
            choice=random.choice(self.inputChoices)
        self.inputChoices.remove(choice)
        return choice
    
    def choose(self):
        choice=random.choice(self.inputChoices)
        self.inputChoices.remove(choice)
        return choice

def main():
    print('Test')
    randomCase=RandomTicTacToe()
    randomCase.randomPlay()
    
    winStatus={'0':0 , '1':0, 'D':0}
    for i in range(randomCase.playNo):
        randomCase2=RandomTicTacToe()
        output=randomCase2.randomPlay()
        if output == 0:
            winStatus['0']+=1
        elif output == 1:
            winStatus['1']+=1
        else:
            winStatus['D']+=1
    print(winStatus)

if __name__=="__main__":main()
    