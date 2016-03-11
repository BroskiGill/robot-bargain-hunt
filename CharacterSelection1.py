from Tkinter import *
master = Tk()

master.resizable(width=FALSE, height=FALSE)
master.geometry('400x400')



def var_states():
   print("Character 1: %d,\nCharacter 2: %d" % (character1_state.get(), character2_state.get()))

Label(master,
             text = "Select your character :",
             font = "Consolas 20 bold").grid(row=0, column = 0, sticky=W)

character1_state = IntVar()
Checkbutton(master,
            text="Character 1",
            font= "Consolas 15",
            variable = character1_state).grid(row=1, sticky=W)

character2_state = IntVar()
Checkbutton(master,
            text="Character 2",
            font="Consolas 15",
            variable = character2_state).grid(row=2, sticky=W)

Button(master,
       text="Play Game",
       font="Consolas 12",
       command=master.quit).grid(row=4, column =0, sticky=W, pady=4)
Button(master,
       text="Submit",
       font="Consolas 12",
       command = var_states).grid(row=3, column =0, sticky = W, pady=4)

mainloop()
