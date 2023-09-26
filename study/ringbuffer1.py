class RingBuffer:
    def __init__(self, size):
        self.buffsize = size
        self.data = [0 for i in range(size)]

    def append(self, x):
        self.data.pop(0)
        self.data.append(x)

    def get(self):
        return self.data

    def mean(self):
        return sum(self.data) / self.buffsize
        #return sum(self.data) / max(len(self.data),1)

# sample usage
if __name__=='__main__':
    buf = RingBuffer(5)
    for i in range(10):
        buf.append(i)
        print(buf.get())
        print(buf.mean())