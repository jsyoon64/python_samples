from tkinter import *
from tkinter import messagebox

import asyncio
import threading

from utils.mysingletone import *


@singleton
class devicelists:
    serialdone_event = None
    req_async_flag_set = None
    async_loop = None


class eclientClient:

    def __init__(self):
        self.comdata = devicelists()

    def __timer반복(self,*args,**kwargs):
        self.t=threading.Timer(1,self.__timer반복)
        self.t.start()

        # if all [self.comdata.req_async_flag_set is not None,self.comdata.serialdone_event is not None, self.comdata.async_loop is not None]:
        if self.comdata.req_async_flag_set is not None:
            if self.comdata.serialdone_event is not None:
                if self.comdata.async_loop is not None:
                    self.comdata.async_loop.call_soon_threadsafe(lambda : self.comdata.serialdone_event.set())
                    self.comdata.req_async_flag_set = None

    def _run(self):
        self.__timer반복()

class eclientGUI:

    def __init__(self):
        self.comdata = devicelists()
        self.client = eclientClient()

        self.master = Tk()
        self.master.title("EVSE Client emulator")
        self.master.resizable(1, 1)

        threading.Thread(target=self.client._run, daemon=True).start()

        buttonT = Button(master=self.master, text='Asyncio Tasks', command=self.do_tasks)
        buttonT.pack()
        buttonX = Button(master=self.master, text='Freezed???', command=self.do_freezed)
        buttonX.pack()


    def do_freezed(self):
        """ Button-Event-Handler to see if a button on GUI works. """
        messagebox.showinfo(message='Tkinter is reacting.')

    def do_tasks(self):
        loop = asyncio.new_event_loop()
        self.comdata.async_loop = loop
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.async_main())
        loop.close()

    async def async_main(self):
        await self._sendasynccmd('debug none\r')
        await self._sendasynccmd('debug hi\r')
        await self._sendasynccmd('debug med\r')

    async def _sendasynccmd(self, string):
        print(string)
        self.comdata.req_async_flag_set = True
        event = asyncio.Event()
        self.comdata.serialdone_event = event        
        await event.wait()
        self.comdata.req_async_flag_set = None
        print('Done...')


if __name__ == "__main__":

    gui = eclientGUI()
    gui.master.mainloop()


