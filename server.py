import SimPy.Simulation as Simulation
import random

class Server():
	def __init__(self, resourceCapacity):
#		self.serviceTime = serviceTime
		self.queueResource = Simulation.Resource(capacity=resourceCapacity, monitored=True)

	def enqueueRequest(self, request):
		executor = Executor(self, request)
		Simulation.activate(executor, executor.run(), Simulation.now())

class Executor(Simulation.Process):
	def __init__(self, server, request):
		self.server = server
		self.request = request
		Simulation.Process.__init__(self, name='Executor')

	def run(self):
		yield Simulation.request, self, self.server.queueResource
		
		service_time = random.expovariate(1.0/0.5)
		print 'Time %.5f: Server start to process the request %d.' % (Simulation.now(), self.request.id)
		yield Simulation.hold, self, service_time
		print 'Time %.5f: Finish processing request %d. A response is going to be sent.' % (Simulation.now(), self.request.id)

		yield Simulation.release, self, self.server.queueResource

		self.request.sigTaskComplete()

