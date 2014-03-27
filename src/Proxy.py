import Globals

class Proxy:
	def __init__(self,name, updater):
		self._alive = True; # so the object can be a ghost 
		self._signals = {} #users reactive signals
		self._1Reactions = [] # one time reactions
		self._gReactions = [] # global reactions
		self._updateSignals = {} #synchronization barrier
		self._updater = updater # function pushes attributes to panda
		Globals.worldObjects.add(self)
		
	def __setattr__(self,name, value):
		
		if name[0] == '_':#if name starts with ._ hand it over to the __dict__
				self.__dict__[name] = value
		else:#if name starts wiht .somethign then put it in signals
				self._updateSignals[name] = value #add check to see if it has already been updated
	def __getattr__(self,name):
		if name[0] == '_':
			return self.__dict__[name]# check for undifined attributes
		else:
			return None# This is where we need to creat observer signals
		#Observer(f) where f is a function that knows which object and which
		#atribute when called it goes in and samples the value
		
	def initialize(self):
		for k,v in self._updateSignals.items():
			self._signals[k] = v.start()
		
	def updater(self):
		self._updater(self)
		
	def react(self,when,what):#when the reaction should happen and what it should do
		if alive:
			when = maybeLift(when)
			self._gReactions.append((when.start(),what))# add to the list
	def react1(self,when,what):#when the reaction should happen and what it should do
		if alive:
			when = maybeLift(when)
			self._1Reactions.append((when.start(),what))# add to the list
		
	def update(self):
		if alive:
			for k,v in self._signals.items():
				v.now()
			thunks = []	
		        for a in self._1Reactions:
		        	temp = a[0].now()
		        	if temp != None:#if it happens remove it from the list
		        		#add thunks
		        		thunks.add(lambda : a[1](self, temp))
		        if(len(thunks) >= 2):
		        	print("Multiple 1 time reactions in a heartbeat")
			for a in self._gReactions:
				temp = a[0].now()
		        	if temp != None:#if it happens remove it from the list
		        		#add thunks
		        		thunks.add(lambda : a[1](self, temp))
		       	self._updateSignals = {} # reset the synchronization barrier and memoization
