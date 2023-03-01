# Machine  Learning - Standard Deviation
# Use Numpy std() method to find the standard deviation
import numpy

speed = [86, 87, 88, 86, 87, 85, 86]

x = numpy.std(speed)

print(x)

# Variance
# Căn bậc hai của phương sai = độ lệch chuẩn
# Use the Numpy var() method to find the variance
import numpy 

speed = [32, 111, 138, 28, 59, 77, 97]

x = numpy.var(speed)
y = numpy.std(speed)

print(x)
print(y)

# Percentiles
# Use the Numpy percentiles() method to find the percentiles
import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 75)

print(x)

