
# Convex unimodal optimization function
from numpy import arange
from matplotlib import pyplot

# Objective function
def objective(x):
    return x[0]**2.0

# Define range for input
r_min, r_max = -5.0, 5.0

# Sample input range uniformly at 0.1 increments
inputs = arange(r_min, r_max, 0.1)

# Compute targets
results = [objective([x]) for x in inputs]

# Create a line plot of input vs result
pyplot.plot(inputs, results)

# Define optimal input value
x_optima = 0.0

# Draw a vertical line at the optimal input
pyplot.axvline(x=x_optima, ls='--', color='red')

# Show the plot
pyplot.xlabel('Input')
pyplot.ylabel('Objective Function Value')
pyplot.title('Objective Function Plot')
pyplot.show()


