# Data Distribution
# Create an array containing 250 random floats between 0 and 5
import numpy

x = numpy.random.uniform(0.0, 5.0, 250)

print(x)

# Histogram
# Draw a histogram

import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5)
plt.show()

# Big Data Distribution
# Create an array with 10000 random numbers 
import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 100000)

plt.hist(x, 100)
plt.show()

# Normal Data Distribution
import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 100000)

plt.hist(x, 100)
plt.show()
