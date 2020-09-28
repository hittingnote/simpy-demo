import SimPy.Simulation as Simulation
import constants
import random

class Client():
	def __init__(self, id):
		self.id = id
	
	def sendRequest(self, request, toServer):
		delay = constants.NW_LATENCY_BASE + \
				random.normalvariate(constants.NW_LATENCY_MU, constants.NW_LATENCY_SIGMA)

		# Send out the request
		requestDeliveryProcess = DeliverRequest()
		Simulation.activate(requestDeliveryProcess, requestDeliveryProcess.run(request, toServer, delay), at=Simulation.now())
		responseHandler = ResponseHandler()
		Simulation.activate(responseHandler, responseHandler.run(request), at=Simulation.now())

class DeliverRequest(Simulation.Process):
	def __init__(self):
		Simulation.Process.__init__(self, name='DeliverRequest')

	def run(self, request, toServer, delay):
		yield Simulation.hold, self, delay
		print 'Time %.5f: Client sends a request %d to the server.' % (Simulation.now(), request.id)
		toServer.enqueueRequest(request)

class ResponseHandler(Simulation.Process):
	def __init__(self):
		Simulation.Process.__init__(self, name='ResponseHandler')

	def run(self, request):
		yield Simulation.hold, self,
		yield Simulation.waitevent, self, request.completionEvent
		# xxx Process xxx
		print 'Time %.5f: A response is received for request %d.' % (Simulation.now(), request.id)

