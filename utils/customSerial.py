"""
파이썬에서 시리얼 통신을 핸들링하기 위해서는 pyserial등의 외부 패키지를 설치해서 사용한다.
pip install pyserial
"""
import serial, serial.tools.list_ports
from threading import Thread

class custSerialThread:
    def __init__(self):
        self._running = False
        self.openedport = None

    """ private run thread """
    def _run(self):
        self._running = True
        while self._running:
            try:
                line = self.openedport.readline()
                # line = self.openedport.read_until(b'\r\n')
                if line:
                    self.updatedata(line)
            except Exception as e:
                print (e)
                pass            

    def close(self):
        self._running = False
        if self.openedport is not None and self.openedport.isOpen() == True:
            self.openedport.close()

    def write(self,data):
        if self.openedport != None:
            self.openedport.write(data)
        else:
            self.show_error('Port is not opened!!!')

    def openrun(self, port) -> tuple[serial.Serial,str]:
        # Open the COM port
        try:
            self.openedport = serial.Serial(port, 460800, timeout=0.1)
        except Exception as ex:
            return None,ex
        else:
            self.close()
            self.openedport.open()

        Thread(target=self._run, daemon=True).start()
        return self.openedport,'successed'

    def isthreadrRunning(self):
        return self._running

    def get_ports(self) -> list:
        Ports = serial.tools.list_ports.comports()
        return [port.name for port in Ports]

    def get_ports_full(self) -> list:
        return serial.tools.list_ports.comports()

    def show_error(self,message):
        raise NotImplementedError()
        
    def updatedata(self,data):
        raise NotImplementedError()
