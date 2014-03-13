import Globals

class Proxy:
	def __init__(self,name):
		self._alive = True;
		self._signals = {}
		self._1Reactions = [] # one time reactions
		self._gReactions = [] # global reactions
		self._updateDict = {}
		Globals.world.add(self)
		
	def __setattr__(self,name, value):
		#if hasattr(self,name):
		#if name starts with ._ hand it over to the __dict__
		#if name starts wiht .somethign then 
		self.updateDict[name] = value
		
		#catch multiple updates on one name in a single heart beat
		
	def react(self):
		if alive:
			pass
		else:
			pass

	def update(self):
		if alive:
			for k,v in _signals:
				v.now()
			for k,v in self._updateDict:
				self.__dict__[k] = v
			self._updateDict = {}
		else:
			pass
