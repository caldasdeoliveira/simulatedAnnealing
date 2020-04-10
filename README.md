# simulatedAnnealing

Simple Python implementation of simulated annealing for work in continuous functions.

## Usage

Import function to desired file and call function: 
	SimulatedAnnealing(cost_function)

Some usage examples can be found in example.py

Function Arguments:

* cost_function: Any function that takes a float as input and returns a float. This is the target function to minimize

* x0: First value to test in the function. Starting position. Defaults to 0.

* alpha: Rate of temperature drop, should be between 0 and 1. Defaults to 0.01. Note that zero is allowed to enable the use of maxiter as the stopping criterion.

* T0: Initial temperature. Temperature drops according to (1-alpha)xT
* Tf: Final temperature. Once the current temperature drops below this value the algorithm stops and an the best result so far is returned.

* neighbourhood_sigma: Standard deviation of the normal distribution used to randomize the next candidate in the neighbourhood. Defaults to 1.

* find_max: Boolean value that indicates if we seek to maximize or minimize the cost function. If we seek to maximize the argument should be true and the cost function will be multiplied by -1 and minimized. Defaults to false.

* maxiter: This argument is not required but has been added as a safety measure against errors in the temperature arguments. This value indicates the maximum number of iterations to be used. Defaults to 1.000.000

## References

The work presented here is based on the information made publicly available in these websites

https://www.youtube.com/watch?v=XNMGq5Jjs5w

https://perso.crans.org/besson/publis/notebooks/Simulated_annealing_in_Python.html

https://en.wikipedia.org/wiki/Simulated_annealing


