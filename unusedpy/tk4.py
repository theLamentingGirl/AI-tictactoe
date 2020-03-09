# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 21:11:10 2020

@author: gaGzy
"""
from tkinter import *

#import tkMessageBox

t = Tk()

def button1_click():
    Label(t,text="Message, Bang!")

def button2_click():
    button1.invoke()

button1 = Button(t, text="Button 1", command=button1_click)
button1.pack()

button2 = Button(t, text="Button 2", command=button2_click)
button2.pack()

mainloop()