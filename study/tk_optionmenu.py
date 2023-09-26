from tkinter import *

OptionList = [
"Aries",
"Taurus",
"Gemini"
]

master = Tk()
master.geometry('300x200')

var = StringVar(master)
var.set(OptionList[0]) # initial value

""" #case 1
option = OptionMenu(master, var, *OptionList)
option.config(width=90, font=('Helvetica', 12))
option.pack()

#labelTest = Label(text="", font=('Helvetica', 12), fg='red')
#labelTest.pack(side="top")

def callback(*args):
    #labelTest.configure(text="The selected item is {}".format(var.get()))
    print(var.get())

var.trace("w", callback)
 """
#case 2

def dropdown_get(sel_val):
    print(sel_val)

option = OptionMenu(master, var, command=dropdown_get, *OptionList)
option.config(width=90, font=('Helvetica', 12))
option.pack()



mainloop()