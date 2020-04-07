import numpy as np
from typing import Callable

def SimulatedAnnealing(cost_function, x0=0, alpha=0.01, T0=100, Tf=1, neighbourhood_sigma=1, find_max=False, maxiter=1000000):
	iteration=0

	if alpha < 0 or alpha>1:
		print("alpha should be between 0 and 1")
		return None
	x = x0
	x_cost = cost_function(x)
	if find_max == True:
		x_cost = -x_cost
	x_best = (x, x_cost)
	T = T0
	while (T > Tf):
		#sample neighbourhood
		x_candidate = np.random.normal(x, neighbourhood_sigma, 1)
		#evaluate new candidate
		x_candidate_cost = cost_function(x_candidate)
		#print("candidate: " + str(x_candidate) + " cost: " + str(x_candidate_cost))
		if find_max == True:
			x_candidate_cost = -x_candidate_cost 
		delta_cost = x_candidate_cost-x_cost
		rand_value = np.random.sample()
		if delta_cost < 0 or rand_value < np.exp(-delta_cost/T):
			x = x_candidate
			x_cost = x_candidate_cost
			if x_cost < x_best[1]:
				x_best = (x, x_cost)
		T -= alpha*T
		if iteration > maxiter:
			print("maxiter reached")
			return None
		iteration += 1
	if find_max == True:
		x_best[1] = -x_best[1]
	return x_best
