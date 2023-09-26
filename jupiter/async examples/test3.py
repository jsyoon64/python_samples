from tkinter import *
from tkinter import messagebox

import asyncio
import threading
import janus

from utils.mysingletone import *


@singleton
class devicelists:
    serialdone_event = None
    req_async_flag_set = None


class eclientClient:

    def __init__(self):
        self.comdata = devicelists()
        self.stopTimerFlag = threading.Event()

    def __timer반복(self,*args,**kwargs):
        if not self.stopTimerFlag.is_set():
            self.t=threading.Timer(1,self.__timer반복)
            self.t.start()

            if self.comdata.req_async_flag_set is not None:
                if self.comdata.serialdone_event is not None:
                    # self.comdata.serialdone_event.set()
                    # self.comdata.serialdone_event.put('a')
                    self.comdata.serialdone_event.sync_q.put('a')
                    # self.comdata.serialdone_event.sync_q.join()
                self.comdata.req_async_flag_set = None

        else:
            pass

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
        # event = asyncio.Event()
        # self.devices.serialdone_event = event
        # loop = asyncio.get_event_loop()
        # loop.run_until_complete(self._sendasynccmd('debug none\r'))
        # loop.close()

        # loop.run_until_complete(self._sendasynccmd('debug hi\r'))
        # loop.run_until_complete(self._sendasynccmd('debug med\r'))
        # asyncio.run(self.async_main())
        # loop = asyncio.new_event_loop()
        # asyncio.set_event_loop(loop)
        # asyncio.get_event_loop().run_until_complete(self.async_main)

        asyncio.run(self._sendasynccmd('debug none\r'))
        asyncio.run(self._sendasynccmd('debug hi\r'))
        asyncio.run(self._sendasynccmd('debug med\r'))



    async def async_main(self):
        await self._sendasynccmd('debug none\r')
        await self._sendasynccmd('debug hi\r')
        await self._sendasynccmd('debug med\r')

    async def _sendasynccmd(self, string):
        print(string)
        waiter_task = asyncio.create_task(self._waitserial())
        await waiter_task
        print('Done...')

    async def _waitserial(self):
        # event = asyncio.Event()
        # event = asyncio.Queue()
        event = janus.Queue()
        self.comdata.serialdone_event = event
        self.comdata.req_async_flag_set = True
        await self.comdata.serialdone_event.async_q.get()
        # await self.comdata.serialdone_event.get()
        # await asyncio.sleep(1)



if __name__ == "__main__":

    gui = eclientGUI()
    gui.master.mainloop()


