from tkinter import *
master = Tk()

master.resizable(width=FALSE, height=FALSE)
master.geometry('400x400')
master.configure(background='Tan')

def var_states():
   print("Indiana Jones %d,\nThe Undertaker: %d" % (character1_state.get(), character2_state.get()))

Label(master,
             text = "Select your character :",
             background= "Tan",
             font = "Consolas 20 bold").grid(row=0, column = 0, sticky=W)

character1_state = IntVar()
Checkbutton(master,
            text="Indiana Jones",
            background= "Tan",
            font= "Consolas 15",
            variable = character1_state).grid(row=1, sticky=W)

character2_state = IntVar()
Checkbutton(master,
            text="The Undertaker",
             background= "Tan",
            font="Consolas 15",
            variable = character2_state).grid(row=2, sticky=W)

Button(master,
       text="Play Game",
       font="Consolas 12",
       background= "wheat",
       command=master.quit).grid(row=4, column =0, sticky=W, pady=4)
Button(master,
       text="Submit",
       background= "wheat",
       font="Consolas 12",
       command = var_states).grid(row=3, column =0, sticky = W, pady=4)

mainloop()
