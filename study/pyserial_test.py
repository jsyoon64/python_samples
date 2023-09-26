"""
파이썬에서 시리얼 통신을 핸들링하기 위해서는 pyserial등의 외부 패키지를 설치해서 사용한다.

pip install pyserial
"""

import serial, serial.tools.list_ports
import tkinter as tk
from tkinter import messagebox
from tkinter import OptionMenu
#from tkinter import *

OpenedPort = None

def dropdown_get(sel_port):
    print(sel_port)

    TargetPort = str(sel_port).split(" ")[0]
    print("[INFO] Use {}...".format(TargetPort))

    # Open the COM port
    try:
        OpenedPort = serial.Serial(TargetPort, 460800, timeout=0)
    except Exception as ex:
        messagebox.showinfo('Error', ex)
    else:
        if(OpenedPort.isOpen() == True):
            OpenedPort.close()
        OpenedPort.open()

        while(True):
            try:
                line = OpenedPort.readline()
                if (line):
                    print(line)         
            except:
                pass


# Get the COM port
Ports = serial.tools.list_ports.comports()

master = tk.Tk()

port_var = tk.StringVar(master)
port_var.set(Ports[0])  # initial value

# Create a OptionMenu
option = OptionMenu(master, port_var, command=dropdown_get, *Ports)
option.config(width=30, font=('Helvetica', 12))
option.grid(column=0, row=0)
option.pack()                                 

master.resizable(1, 1)
master.mainloop()
