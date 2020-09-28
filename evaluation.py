import SimPy.Simulation as Simulation
import client
import server
import workload

def runExperiment():
	Simulation.initialize()
	c = client.Client(1)
	s = server.Server(1)
	w = workload.Workload(c, s)

	Simulation.activate(w, w.run(), at=Simulation.now())
	Simulation.simulate(until=50.0)

if __name__ == '__main__':
	runExperiment()

