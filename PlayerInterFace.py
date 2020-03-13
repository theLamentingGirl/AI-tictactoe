# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 21:17:04 2020

@author: gaGzy
@author: wridhdhi
"""

from GameEngine import *

#=============================================================================

class playerInterface(playTicTacToe):
    def __init__(self):

        super().__init__()
        self.player=0
        self.parent=Tk()


    #partition1 for other buttons
        self.partition1=Frame(self.parent)
        self.partition1.pack(side=TOP)
        
        self.quitButton=Button(self.partition1,text="QUIT",padx=10,pady=2,command=self.parent.destroy)
        self.quitButton.pack(side=RIGHT)

#shows which player to play
        self.playerBox=Label(self.partition1)
        self.playerBox.pack(side=RIGHT)

        self.textBox=Label(self.partition1,text="make a move")
        self.textBox.pack(side=RIGHT)
        
        self.resetButton=Button(self.partition1,text="RESET",padx=10,pady=2,command=self.reset)
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
        self.button1=Button(self.bottomframe,padx=50,pady=50,command=lambda:self.clickButton(self.button1,'button1'))
        self.button1.pack(side=LEFT)
        
        
        #button2
        self.button2=Button(self.bottomframe,padx=50,pady=50,command=lambda:self.clickButton(self.button2,'button2'))
        self.button2.pack(side=LEFT)
        
        #button3
        self.button3=Button(self.bottomframe,padx=50,pady=50,command=lambda:self.clickButton(self.button3,'button3'))
        self.button3.pack(side=LEFT)
        
        #button4
        self.button4=Button(self.midframe,padx=50,pady=50,command=lambda:self.clickButton(self.button4,'button4'))
        self.button4.pack(side=LEFT)
        
        #button5
        self.button5=Button(self.midframe,padx=50,pady=50,command=lambda:self.clickButton(self.button5,'button5'))
        self.button5.pack(side=LEFT)
        
        #button6
        self.button6=Button(self.midframe,padx=50,pady=50,command=lambda:self.clickButton(self.button6,'button6'))
        self.button6.pack(side=LEFT)
        
        #button7
        self.button7=Button(self.topframe,padx=50,pady=50,command=lambda:self.clickButton(self.button7,'button7'))
        self.button7.pack(side=LEFT)
        
        #button8
        self.button8=Button(self.topframe,padx=50,pady=50,command=lambda:self.clickButton(self.button8,'button8'))
        self.button8.pack(side=LEFT)

        #button9
        self.button9=Button(self.topframe,padx=50,pady=50,command=lambda:self.clickButton(self.button9,'button9'))
        self.button9.pack(side=LEFT)
        
        self.userStartButton=Button(self.partition1,padx=10,pady=2,text="User Start")
        self.userStartButton.pack(side=LEFT)

        self.compStartButton=Button(self.partition1,padx=10,pady=2,text="Comp Start")
        self.compStartButton.pack(side=LEFT)
        

        self.buttonVal={"button1":'00',"button2":'01',"button3":'02',"button4":'10',\
                   "button5":'11',"button6":'12',"button7":'20',"button8":'21',\
                   "button9":'22'}
 #       self.parent.mainloop()


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

    def clickButton(self,whichbutton,buttonname):

        ''' Loop iterates until game is won/loss/draw
        else keep playing'''
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

            whichbutton["text"]=textToPut
            whichbutton.configure(state=DISABLED)

            self.winner()


            # CHANGE PLAYERBOX
            print('if he made a valid move:',didhe)
            if didhe==True:
                self.player=int(not(self.player))

#                if self.checkWin()==True:
        print(self.gameArea)

    def winner(self):
        winStatus=self.checkWin()
        if winStatus[0]==True:
            self.disableAll()
            if self.player==0:
                textToPut='O'
            else:
                textToPut='X'
#            print("player",self.player,"text",textToPut)
            self.playerBox.configure(text=textToPut)
            if winStatus[1]=='':
                self.playerBox.configure(text='')
                return self.textBox.configure(text='Draw')
            else:
                return self.textBox.configure(text='won the game')
    
    def reset(self):
        self.player=0
        self.gameArea=np.empty((3,3))
        self.gameArea.fill(None)
        self.button1.configure(state=NORMAL,text="",command=lambda:self.clickButton(self.button1,"button1"))
        self.button2.configure(state=NORMAL,text="",command=lambda:self.clickButton(self.button2,"button2"))
        self.button3.configure(state=NORMAL,text="",command=lambda:self.clickButton(self.button3,"button3"))
        self.button4.configure(state=NORMAL,text="",command=lambda:self.clickButton(self.button4,"button4"))
        self.button5.configure(state=NORMAL,text="",command=lambda:self.clickButton(self.button5,"button5"))
        self.button6.configure(state=NORMAL,text="",command=lambda:self.clickButton(self.button6,"button6"))
        self.button7.configure(state=NORMAL,text="",command=lambda:self.clickButton(self.button7,"button7"))
        self.button8.configure(state=NORMAL,text="",command=lambda:self.clickButton(self.button8,"button8"))
        self.button9.configure(state=NORMAL,text="",command=lambda:self.clickButton(self.button9,"button9"))
        self.userStartButton.configure(state=NORMAL,text='User Play ')
        self.compStartButton.configure(state=NORMAL,text='Comp Play')
        self.playerBox.configure(text="")
        self.textBox.configure(text="make a move")
        self.inputChoices=['00','01','02','10','11','12','20','21','22']
        


#MAIN FUNCTION

def main():
    
#    playState=np.array([[1,0,1],[0,1,0],[0,0,1]])
#    playState2=np.array([[0,0,1],[0,1,0],[0,1,1]])
    playState3=np.array([[1,0,1],[0,1,0],[0,1,0]])
    testPlay=playTicTacToe(playState3)
    testPlay.play()
    
    
    #HOW TO TEST THE GAME for player1 and player 2
    PlayerGame=playerInterface()
#    PlayerGame.play()
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
