# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 15:59:15 2020

@author: gaGzy
"""

from tkinter import *

#root= Tk()
#widget = Button(root,text='Spam', padx=10, pady=10)
#widget.pack(padx=20, pady=20)
#widget.config(cursor='gumby')
#widget.config(bd=8, relief=RAISED)
#widget.config(bg='dark green', fg='white')
#widget.config(text='Not spam',font=('helvetica', 20, 'underline italic'))
#root.mainloop()

#from Tkinter import *                   

#class Hello(Frame):                     ##???
#    def __init__(self, parent=None):    
#        Frame.__init__(self, parent)
#        self.pack()
#        self.make_widgets()
#
#    def make_widgets(self):             
#        widget = Button(self, text='Hello world')#, command=self.quit)
#        widget.pack(side=LEFT)
#
#if __name__ == '__main__':  Hello().mainloop()
#
#from tkinter import *
#
#root = Tk()
#frame = Frame(root)
#frame.pack()
##
#bottomframe = Frame(root)
#bottomframe.pack( side = BOTTOM )
#
#redbutton = Button(frame, text="Red", fg="red")
#redbutton.pack( side = LEFT)
#
#
#bluebutton = Button(frame, text="Blue", fg="blue")
#bluebutton.pack( side = LEFT )
#
#
#brownbutton = Button(frame, text="Brown", fg="brown")
#brownbutton.pack( side = LEFT )
#
#blackbutton = Button(bottomframe, text="Black", fg="black")
#blackbutton.pack( side = BOTTOM)
#
#root.mainloop()

#from Tkinter import *                   

#
#class Hello(Frame):
##    widget = Button(root,text='OK')
##    widget.pack(side=LEFT)
##frame.pack()
#    
#    def __init__(self, parent=None):
#        self.buttonname=['red','blue','brown']
#        self.buttons=[]
#        print('a new object is being created')
#        Frame.__init__(self, parent)
##        self.frame = Frame(parent)
##        self.bottomframe = Frame(parent)
##        self.frame.pack()
#        self.pack()
#        self.make_widgets()
##        self.bottomframe.pack( side = BOTTOM )
##        self.redbutton = Button(self.frame, text="Red", fg="red")
##        for i,name in enumerate(self.buttonname):
##            self.buttons.append(Button(self.frame))
##            self.buttons[i].pack(side=LEFT)
##        self.redbutton.pack( side = LEFT)
##        self.bluebutton = Button(self.frame, text="Blue", fg="blue")
##        self.bluebutton.pack( side = LEFT )
##        self.brownbutton = Button(self.frame, text="Brown", fg="brown")
##        self.brownbutton.pack( side = LEFT )
##        self.blackbutton = Button(self.bottomframe, text="Black", fg="black")
##        self.blackbutton.pack( side = BOTTOM)
#        
#
##
##    def callWidget(self):
##        print("DUH")
##        i=0
##        self.buttons[i].configure(state=NORMAL,command=self.calledWidget(i))
##        
#    def calledWidget(self,i=0):
#        print("called for button",i)
#        self.buttons[i].configure(state=DISABLED,background='black')
#        #)#,activebackground='black')
##        self.redbutton.configure(state=DISABLED)
##        self.bluebutton.configure(state=DISABLED)
##        self.brownbutton.configure(state=DISABLED)
##        self.blackbutton.configure(state=DISABLED)
#
#    def make_widgets(self):
#        print("making widget")
#        for i,name in enumerate(self.buttonname):
#            self.buttons.append(Button(self,text=name, background=name))
#            self.buttons[i].pack(side=LEFT)
##        self.buttons[0].configure(state=NORMAL,command=self.calledWidget(0))
##        widget.configure(state=DISABLED, background='red')
##        for i,name in enumerate(self.buttons):
##            self.buttons[i].configure(text=self.buttonname[i], background=self.buttonname[i],state=NORMAL,command=self.calledWidget(i))
##       self.buttons[1].configure(state=NORMAL, background='blue',command=self.quit)
##        self.brownbutton.configure(state=NORMAL, background='brown',command=self.callWidget)
##        self.blackbutton.configure(state=NORMAL, background='black',command=self.callWidget)
##        self.widget.focus_set()
#
#if __name__ == '__main__':  Hello().mainloop()

#
#class Hello(Frame):
#    def __init__(self, parent=None):
#        Frame.__init__(self, parent)
#        self.pack()
#        self.make_widgets()
#
#    def call_widget(self):
#        print("Duh")
#        self.widget.configure(background='blue',state=DISABLED)
#
#    def make_widgets(self):             
#        self.widget = Button(self, text='Hello world',bg='yellow', fg='blue',command=self.call_widget)#, command=self.quit)
#        self.Quit = Button(self, text = "QUIT", command = self.master.destroy)
#        self.widget.pack(side=LEFT)
#        self.Quit.pack(side=LEFT)
#
#
#if __name__ == '__main__':  Hello().mainloop()
