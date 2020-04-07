from simulatedAnnealing import *

def CostFunction(x):
	return (x-1)**2


ans =  SimulatedAnnealing(CostFunction)
print("function: (x-1)**2 x_best=" + str(ans[0]) + " x_cost: " + str(ans[1]) )


def CostFunction(x):
	return max(0,-x)


ans =  SimulatedAnnealing(CostFunction, x0=-10)
print("function: max(0,-x) x_best=" + str(ans[0]) + " x_cost: " + str(ans[1]) )

def CostFunction(x):
	return min(x**2, -(x-1)**2+10)


ans =  SimulatedAnnealing(CostFunction, find_max=True)
print("function: min(x**2, -(x-1)**2+10) x_best=" + str(ans[0]) + " x_cost: " + str(ans[1]) )
