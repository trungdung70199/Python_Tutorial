# Machine Learning
# Mean - Median - Mode
# Mean: The mean value is the average value
import numpy
speed = [99, 86, 87, 90, 77, 88, 89, 100, 92, 95]
x = numpy.mean(speed)

print(x)

# Median: The median value is the value in the middle
import numpy
speed = [99, 86, 87, 88, 89, 90, 100, 102, 77, 76, 75]
x = numpy.median(speed)

print(x)

# If there are two numbers in the middle divide the 
# sum of those  numbers by two
import numpy

speed = [99, 86, 87, 88, 86, 103, 87, 94, 78, 77, 85, 86]
x = numpy.median(speed)

print(x)

# Mode: The mode value is the value that append the most number of time
# Use Scipy() method
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = stats.mode(speed)

print(x)