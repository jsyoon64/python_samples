from tkinter import *

class MyLabel(Label):
    def __init__(self,*args,**kwargs):
        if not kwargs:
            kwargs = dict()
        if not 'width' in kwargs:
            kwargs['width'] = 9            
        #if not 'height' in kwargs:
        #    kwargs['height'] = 10            
        #kwargs['font'] = ("Arial",16)
        if not 'fg' in kwargs:
            kwargs['fg'] = 'blue'

        if not 'justify' in kwargs:
            kwargs['justify'] = 'center'

        if not 'relief' in kwargs:
            kwargs['relief'] = GROOVE
            
        super().__init__(*args, **kwargs)
