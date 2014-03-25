import Globals

class Proxy:
	def __init__(self,name):
		self._alive = True; # so the object can be a ghost 
		self._signals = {} #users reactive signals
		self._1Reactions = [] # one time reactions
		self._gReactions = [] # global reactions
		self._updateDict = {} # synchronization barrier
		self._updateSignals = {} #synchronization barrier
		self._alreadyUpdated = [] # form memoization of setattr
		Globals.world.add(self)
		
	def __setattr__(self,name, value):
		
		if name[1] == '_':#if name starts with ._ hand it over to the __dict__
				self.updateDict[name] = value
		else:#if name starts wiht .somethign then put it in signals
				self._signals[name] = value
		
			
		if name in alreadyUpdated:#catch multiple updates on one name in a single heart beat
			print(name+" has already been updated")
		
		else:
			alreadyUpdated.append(name)
		
		
	def react(self):
		if alive:
			pass
		else:
			pass

	def update(self):
		if alive:
			for k,v in self._updateSignals:
				 self._signals[k] = v
			for k,v in self._updateDict:
				self.__dict__[k] = v
		        self._updateSignals = {} # reset the synchronization barrier and memoization
			self._updateDict = {}
			self.alreadyUpdated = []
			for k,v in _signals:
				v.now()for k,v in _signals:
				v.now()
		else:
			pass
