import SimPy.Simulation as Simulation

class Request():
	def __init__(self, id):
		self.id = id
		self.completionEvent = Simulation.SimEvent("ClientToServerCompletion")
	
	def sigTaskComplete(self, piggyBack=None):
		if(self.completionEvent is not None):
			self.completionEvent.signal(piggyBack)

