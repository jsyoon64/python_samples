
class ObserveList:
    def __init__(self):
        self._value = list()
        self._callbacks = list()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value:list):
        self._value.clear()
        self._value = new_value.copy()
        self._notify()
    
    def _notify(self):
        for cb in self._callbacks:
            cb(self._value)

    def reg_cb(self, callback):
        self._callbacks.append(callback)

if __name__ == "__main__":

    def display_list(data:list):
        print(f'{data=}')

    l1 = ObserveList()
    l1.reg_cb(display_list)

    l1.value = [1,2,3]
    l1.value = [4,5,6]

