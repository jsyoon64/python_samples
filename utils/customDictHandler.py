from collections import defaultdict

class MyDictHandler(object):

	def __init__(self):
		self.__eventhandlersample = defaultdict(list)
	
	"""
	def setkey(self, value):
		self.__keyvalue = value
		
	def __iadd__(self, Ehandler): 
		self.__eventhandlersample[self.__keyvalue].append(Ehandler) 
		return self

	def __isub__(self, Ehandler): 
		self.__eventhandlersample[self.__keyvalue].remove(Ehandler) 
		return self

	def __call__(self, event_type, *args, **keywargs): 
		if event_type in self.__eventhandlersample:
			for eventhandlersample in self.__eventhandlersample[self.__keyvalue]: 
				eventhandlersample(*args, **keywargs)     
	"""
	def addhandler(self, event_type, Ehandler):
		self.__eventhandlersample[event_type].append(Ehandler)
		return self

	def removehandler(self, event_type, Ehandler):
		self.__eventhandlersample[event_type].remove(Ehandler)
		return self

	def __call__(self, event_type, *args, **keywargs): 
		if event_type in self.__eventhandlersample:
			for eventhandlersample in self.__eventhandlersample[event_type]: 
				eventhandlersample(*args, **keywargs)                 

	def get(self, event_type):
		return list( map(lambda x :x, self.__eventhandlersample[event_type]) )

	def __repr__(self):
		ret_string = str()
		for event_type in self.__eventhandlersample:
			ret_string += str(event_type) + ':\n'
			#ret_string += ','.join(map(lambda x:str(x),self.__eventhandlersample[event_type]))
			#ret_string += ','.join(map(lambda x:str(x.__name__),self.__eventhandlersample[event_type]))
			ret_string += ','.join(map(lambda x:str(x.__qualname__),self.__eventhandlersample[event_type]))
			ret_string += '\n'

		return ret_string
		#return ",".join( map(lambda x : x + str(self.__eventhandlersample[x]), self.__eventhandlersample) )
		
if __name__ == "__main__":

	def ex1(asd):
		print("ex1",asd)

	def ex2(asd):
		print("ex2",asd)

	ex1handler = MyDictHandler()
	# ex1handler.setkey('dload')
	# ex1handler += ex1
	# ex1handler += ex2

	ex1handler.addhandler('dload', ex1)
	ex1handler.addhandler('dload', ex2)

	ex1handler('dload','after +')
	# ex1handler -= ex2
	ex1handler.removehandler('dload', ex2)

	ex1handler('dload','after -')

