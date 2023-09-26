from tkinter import *
from tkinter import messagebox
import asyncio
import random

def do_freezed():
    """ Button-Event-Handler to see if a button on GUI works. """
    messagebox.showinfo(message='Tkinter is reacting.')

def do_tasks():

    tkmain = asyncio.ensure_future(tk_main(root))
    rdmain = asyncio.ensure_future(do_urls())

    """ Button-Event-Handler starting the asyncio part. """
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(do_urls())
    finally:
        loop.close()
        
async def tk_main(root):
    while True:
        root.update()
        await asyncio.sleep(0.05)

async def one_url(url):
    """ One task. """
    sec = random.randint(1, 15)
    await asyncio.sleep(sec)
    return 'url: {}\tsec: {}'.format(url, sec)

async def do_urls():
    """ Creating and starting 10 tasks. """
    tasks = [
        one_url(url)
        for url in range(2)
    ]
    completed, pending = await asyncio.wait(tasks)
    results = [task.result() for task in completed]
    print('\n'.join(results))


if __name__ == '__main__':
    root = Tk()

    buttonT = Button(master=root, text='Asyncio Tasks', command=do_tasks)
    buttonT.pack()
    buttonX = Button(master=root, text='Freezed???', command=do_freezed)
    buttonX.pack()

    root.mainloop()