
class MyEvtHandler(object):
	def __init__(self):
		self.__eventhandlersample = []
	
	def __iadd__(self, Ehandler): 
		self.__eventhandlersample.append(Ehandler) 
		return self

	def __isub__(self, Ehandler): 
		self.__eventhandlersample.remove(Ehandler) 
		return self

	def __call__(self, *args, **keywargs): 
		for eventhandlersample in self.__eventhandlersample: 
			eventhandlersample(*args, **keywargs)                 

	#def get(self):
	def __repr__(self):
		#return ",".join( map(lambda x :str(x.__name__), self.__eventhandlersample) )
		return ",".join( map(lambda x :str(x.__qualname__), self.__eventhandlersample) )

if __name__ == "__main__":

	def ex1(asd):
		print("ex1",asd)

	def ex2(asd):
		print("ex2",asd)

	ex1handler = MyEvtHandler()
	ex1handler += ex1
	ex1handler += ex2

	ex1handler('after +')
	ex1handler -= ex2

	ex1handler('after -')

