# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 22:05:06 2020

@author: gaGzy



"""
A={"button1":'00',"button2":'01',"button3":'02'}

pos=A['button3']
print(pos[0]+pos[1])


buttonIndex={'00':"button1",'01':"button2",'02':"button3",'10':"button4",\
              '11':"button5",'12':"button6",'20':"button7",'21':"button8",\
              '22':"button9"}
pos=pos[0]+pos[1]

pos=str(i)+str(j)
buttonval=buttonIndex[pos]
print(buttonval)

i=1
j=2
pos=str(i)+str(j)
print(pos,type(pos))

fl