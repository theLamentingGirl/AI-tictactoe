# BASICS OF TKINTER

`Tkinter` is a graphical user interface(GUI) library in python which makes life easier.

A GUI through tkinter can be made by 3 steps

1. Create a window where all your elememts of GUI must go into.

- this involves creating 'parent' window which is the primary window that is constantly displayed when the GUI is being run and gets terminated when window closed. 
- contains the Frames and Subframes to hold other objects.

2. Create required widgets and pack them onto the window created. 
- widgets include `Buttons`=create buttons,`Labels`=create text boxes,`Canvas`=2D structures,`Entry`=for entering input,etc.(This list would be updated as different things are being learnt.)
- All created widgets needs to be assigned a position in the window which is done by `pack`,`grid`,`place`.

3. Run mainloop to keep the window running and constantly visible.
- When window is closed the mainloop terminates.

`from tkinter import *`
## 1. GUI Window

`root=Tk()`importing class Tk which has all required widgets and frames.
`f1 = Frame(root)` setting up a frame
`f1.pack(side=LEFT/RIGHT/TOP/BOTTOM)` Shoves the frame created onto the main window(here it's 'root')

## 2. 
### A. Widgets

`newButton=Button(root,text='',bg='some color',fg='some color',padx,pady,command=funcname)` 
- root specifies the location where button is being placed.
- avoid writing as funcname()
- command func is executed upon clicking the button
- lambda is a temprary instance of a function which can be reset. It's a python thing.
- padx and pady help in resizing 

`newText=Label(root,text='',bg='',fg='',)`
- shows a textbox.
- default size of the textbox is len of text. Can be changed.

`input=Entry(root,text='',bg='',fg='')`
- text here shows '' in the input box which can be deleted and our input can be written.

'myCanvas=Canvas(-- fill it up--)

### B. Placers
Used to position the widgets.

`widget.pack(side=LEFT/RIGHT/TOP/BOTTOM)`
- pack shoves widget onto the screen. 
- if more than 1 pack, arrangement is relative.

`widget.grid(row=x,column=y,padx='',pady='')`
- rows and cols assign position-grid format

`widget.place() `


### Main Loop

`root.mainloop()`
