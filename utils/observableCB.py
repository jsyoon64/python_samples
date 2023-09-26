class Subject:
    """Represents what is being observed"""
    def __init__(self):
        """create an empty observer list"""
        self._observers = []
 
    def notify(self):
        """Alert the observers"""
        for observer in self._observers:
            observer(self)
 
    def attach(self, observer):
        """If the observer is not in the list,
        append it into the list"""
        if observer not in self._observers:
            self._observers.append(observer)
 
    def detach(self, observer):
        """Remove the observer from the observer list"""
        try:
            self._observers.remove(observer)
        except ValueError:
            pass
 
 
 
class ObserveData(Subject):
    """monitor the object"""
    __slots__ = ['name','_data']

    def __init__(self, name=''):
        Subject.__init__(self)
        self._data = 0
        self.name = name
 
    @property
    def data(self):
        return self._data
 
    @data.setter
    def data(self, value):
        self._data = value
        self.notify()
 

if __name__ == "__main__":
 
    """provide the data"""
    obj1 = ObserveData('Data 1')
    obj2 = ObserveData('Data 2')
    
    def HexViewer(subject):
        # print('HexViewer: Subject {} has data {}'.format(subject.name, subject.data))
        print('HexViewer: Subject {} has data 0x{:x}'.format(subject.name, subject.data))

    def DecimalViewer(subject):
        # print('DecimalViewer: Subject {} has data {}'.format(subject.name, subject.data))
        print('DecimalViewer: Subject %s has data %d'%(subject.name, subject.data))


    obj1.attach(HexViewer)
    obj1.attach(DecimalViewer)
 
    obj2.attach(HexViewer)
    obj2.attach(DecimalViewer)
 
    # obj1.data = 'test'
    obj1.data = 10
    obj2.data = 15
