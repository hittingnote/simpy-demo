import SimPy.Simulation as Simulation
import random
import request
import numpy

class Workload(Simulation.Process):
	def __init__(self, client, server):
		self.client = client
		self.server = server
		self.numRequest = 0
		Simulation.Process.__init__(self, name='Workload')
	
	def run(self):
		while True:
			yield Simulation.hold, self, 
			req= request.Request(self.numRequest)
			self.numRequest += 1
			self.client.sendRequest(req, self.server)

			yield Simulation.hold, self, numpy.random.poisson(1.0)

