from tkinter import *
from tkinter import messagebox

import asyncio
import threading

from utils.mysingletone import *


@singleton
class devicelists:
    req_async_flag_set = None
    async_event = asyncio.Event()
    async_loop = asyncio.new_event_loop()

    def __init__(self) -> None:
        asyncio.set_event_loop(self.async_loop)
        pass



class eclientClient:

    def __init__(self):
        self.comdata = devicelists()

    def __timer반복(self,*args,**kwargs):
        self.t=threading.Timer(5,self.__timer반복)
        self.t.start()

        # if all [self.comdata.req_async_flag_set is not None,self.comdata.serialdone_event is not None, self.comdata.async_loop is not None]:
        if self.comdata.req_async_flag_set is not None:
            self.comdata.async_loop.call_soon_threadsafe(lambda : self.comdata.async_event.set())
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
        self.master.minsize(200,200)

        threading.Thread(target=self.client._run, daemon=True).start()

        buttonT = Button(master=self.master, text='Asyncio Tasks', command=self.do_tasks)
        buttonT.pack()


    def do_tasks(self):
        self.comdata.async_loop.run_until_complete(self.async_main())

    async def async_main(self):
        await self._sendasynccmd('debug none\r')
        await self._sendasynccmd('debug hi\r')
        await self._sendasynccmd('debug med\r')

    async def _sendasynccmd(self, string):
        print(string)
        self.comdata.req_async_flag_set = True 
        self.comdata.async_event.clear()
        await self.comdata.async_event.wait()
        self.comdata.req_async_flag_set = None
        print('Done...')


if __name__ == "__main__":

    gui = eclientGUI()
    gui.master.mainloop()


