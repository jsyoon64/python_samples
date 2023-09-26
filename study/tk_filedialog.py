"""
Open a file dialog window in tkinter using the filedialog method.
Tkinter has a prebuilt dialog window to access files. 
This example is designed to show how you might use a file dialog askopenfilename
and use it in a program.
"""

from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename

#This is where we lauch the file manager bar.
def OpenFile():
    name = askopenfilename(initialdir="c:/work/python/",
                           filetypes =(("Text File", "*.txt"),("All Files","*.*")),
                           title = "Choose a file."
                           )
    print (name)
    #Using try in case user types in unknown file or closes without choosing a file.
    try:
        with open(name,'r') as UseFile:
            print(UseFile.read())
    except:
        print("No file exists")


root = Tk()
Title = root.title("File Opener")
root.geometry("640x400")
root.resizable(False, False)
label = ttk.Label(root, text ="file open dialog example",font=("Helvetica", 12))
label.pack()

#Menu Bar
menu = Menu(root)

root.config(menu=menu)

file = Menu(menu)

file.add_command(label = 'debug none', command = OpenFile)
file.add_command(label = 'debug hi', command = lambda:exit())
file.add_command(label = 'debug med', command = lambda:exit())

menu.add_cascade(label = 'Debug Command', menu = file)

root.mainloop()
