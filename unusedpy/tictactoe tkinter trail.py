# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 02:43:08 2020

@author: gaGzy
"""
from tkinter import *

root= Tk()

def myFunc():
    txt="x"
    myLabel=Label(root,text=txt)
#    #shove text onto the window
    myLabel.pack()

myButton=Button(root,text="OK",command=quit)
myButton.pack()
root.mainloop()