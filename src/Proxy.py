import Globals

class Proxy:
	def __init__(self,* named, ** unnamed):
		self.alive = True;
		self.signals = {}
		self.reactions = {}
	def __setattr__(self,name, value):
		#if hasattr(self,name):
		self.updateDict[name] = value
		
	def react(self):
		if alive:
			pass
		else:
			pass
	def update(self):
		if alive:
			for k,v in signals:
				v.now()
			for k,v in self.updateDict:
				self.__dict__[k] = v
		else:
			pass
