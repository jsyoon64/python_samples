"""
파이썬에서 시리얼 통신을 핸들링하기 위해서는 pyserial등의 외부 패키지를 설치해서 사용한다.

pip install pyserial
"""

import serial, serial.tools.list_ports
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as tkst
from tkinter import messagebox
from tkinter import OptionMenu
from threading import Thread
#from tkinter import *

OpenedPort = None

def dropdown_get(sel_port):
    global OpenedPort
    print(sel_port)

    TargetPort = str(sel_port).split(" ")[0]
    print("[INFO] Use {}...".format(TargetPort))
  
    if (sr.isThreadRunning()):
        print('thread is Run, stop')
        OpenedPort.close()
        sr.terminate()

    # Open the COM port
    try:
        OpenedPort = serial.Serial(TargetPort, 460800, timeout=0)
    except Exception as ex:
        messagebox.showinfo('Error', ex)
    else:
        if(OpenedPort.isOpen() == True):
            OpenedPort.close()
        OpenedPort.open()

    SerPrtThr = Thread(target=sr.run, args=(OpenedPort,))
    SerPrtThr.start()    
        
def SerialWrite(data):
    OpenedPort.write(data)

class SerialDisplayThread:
    def __init__(self):
        self._running = False

    def terminate(self):
        self._running = False

    def isThreadRunning(self):
        return self._running

    def run(self, port):
        self._running = True
        while self._running:
            try:
                line = port.readline()
                if (line):
                    print(line)
                    # insert text in a scrolledtext                    
                    scrt.insert(tk.INSERT, line)        
                    scrt.see(tk.END)
                    #time.sleep(1)                  
            except:
                pass            
  

# Get the COM port
Ports = serial.tools.list_ports.comports()
sr = SerialDisplayThread()

master = tk.Tk()
#master.geometry('300x200')

port_var = tk.StringVar(master)
port_var.set(Ports[0])  # initial value

# Create a OptionMenu
option = OptionMenu(master, port_var, command=dropdown_get, *Ports)
#option.config(font=('Helvetica', 12))
option.grid(column=0, row=0)
#option.pack()

# Create a scrolledtext
scrt = tkst.ScrolledText(master, width=80, height=10, wrap=tk.WORD)
scrt.grid(column=0, row=1, columnspan=3)
#scrt.pack()
scrt.focus_set()                                          

btntext = 'debug med\r'.encode('utf-8')
btn1 = tk.Button(text=btntext)
btn1.grid(column=1, row=0)
btn1.config(command=lambda tet = btntext: SerialWrite(tet))

btntext = 'debug hi\r'.encode('utf-8')
btn2 = tk.Button(text='debug hi')
btn2.grid(column=2, row=0)
btn2.config(command=lambda tet = btntext: SerialWrite(tet))

master.resizable(1, 1)
master.mainloop()

sr.terminate()