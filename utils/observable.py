#class 선언 위치 에러 fix 하는 lib
from __future__ import annotations
from abc import ABC, abstractmethod

class Subject:
    """Represents what is being observed"""
    def __init__(self):
        """create an empty observer list"""
        self._observers = []
 
    def notify(self, modifier = None):
        """Alert the observers"""
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)
 
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
 
 
 
class Data(Subject):
    """monitor the object"""
    def __init__(self, name =''):
        Subject.__init__(self)
        self.name = name
        self._data = 0
 
    @property
    def data(self):
        return self._data
 
    @data.setter
    def data(self, value):
        self._data = value
        self.notify()
 

class Observer(ABC):
    """ The Observer interface declares the update method, used by subjects. """
    @abstractmethod
    def update(self, subject: Subject) -> None:
        """ Receive update from subject.    """
        pass




if __name__ == "__main__":
 
    """provide the data"""
    obj1 = Data('Data 1')
    obj2 = Data('Data 2')
 
    class HexViewer(Observer):
        """updates the Hewviewer"""
        def update(self, subject):
            print('HexViewer: Subject {} has data 0x{:x}'.format(subject.name, subject.data))

    class DecimalViewer(Observer):
        """updates the Hewviewer"""
        def update(self, subject):
            print('DecimalViewer: Subject {} has data 0x{:x}'.format(subject.name, subject.data))

    view1 = DecimalViewer()
    view2 = HexViewer()
 
    obj1.attach(view1)
    obj1.attach(view2)
 
    obj2.attach(view1)
    obj2.attach(view2)
 
    obj1.data = 10
    obj2.data = 15