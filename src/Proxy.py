import Globals

class Proxy:
	def __init__(self,name):
		self._alive = True; # so the object can be a ghost 
		self._signals = {} #users reactive signals
		self._1Reactions = [] # one time reactions
		self._gReactions = [] # global reactions
		self._updateSignals = {} #synchronization barrier
		
		Globals.world.add(self)
		
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
		
	def react(self,when,what):#when the reaction should happen and what it should do
		if alive:
			self._gReactions.append((what,when))# add to the list
	def react1(self,when,what):#when the reaction should happen and what it should do
		if alive:
			self._1Reactions.append((what,when))# add to the list
		
	def update(self):
		if alive:
			
			for k,v in _signals:
				v.now()for k,v in _signals:
				v.now()
				
		        for a in 1Reactions:
		        	#if it happens remove it from the list
			for a in gReactions:
				#leave them in
			for k,v in self._updateSignals:
				 self._signals[k] = v
			
		         self._updateSignals = {} # reset the synchronization barrier and memoization
		
