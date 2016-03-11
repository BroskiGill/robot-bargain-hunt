from Tkinter import *

root = Tk()
root.resizable(width=FALSE, height=FALSE)
root.geometry('400x400')

###
logo = PhotoImage(file="assets/player-idea.gif")
w1 = Label(root, image=logo).pack(side="right")
###

###
title = """Character Selection:"""
w2 = Label(root, 
           justify=LEFT,
           padx = 10, 
           text=title,
           font = "Consolas 20 bold").pack(side="top")
###

###
character1_state = IntVar()
Checkbutton(root,
            text="Character 1",
            font= "Consolas 15",
            variable = character1_state).pack(side="left")
###

###

###

###
character2_state = IntVar()
Checkbutton(root,
            text="Character 2",
            font="Consolas 15",
            variable = character2_state).pack(side="left")
###

###
explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily."""
w2 = Label(root, 
           justify=LEFT,
           padx = 10, 
           text=explanation).pack(side="left")
###
root.mainloop()
