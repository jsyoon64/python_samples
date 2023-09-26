
class ObserveList:
    def __init__(self):
        self._value = list()
        self._event_key = None
        self._frame = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value:list):
        self._value.clear()
        self._value = new_value.copy()
        self._notify()
    
    def _notify(self):
        if self._event_key is not None and self._frame is not None:
            self._frame.event_generate(self._event_key)

    def reg_event(self, guiframe, key):
        self._event_key = key
        self._frame = guiframe


if __name__ == "__main__":
    import tkinter

    root = tkinter.Tk()

    l1 = ObserveList()
    l1.reg_event(root,'<<TEST>>')

    def test1():
        l1.value = [1,2,3]

    def label_config(event):
        label.configure(text='pressed')
        print(l1.value)    
    
    root.bind('<<TEST>>', label_config)


    label = tkinter.Label(root)
    label.pack()

    button = tkinter.Button(root, width = 15, text='button',command=test1)
    button.pack()

    root.mainloop()

