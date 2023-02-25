# Matplotlib Tutorial
# Check Matplotlib Version
import matplotlib
print(matplotlib.__version__)

# Pyplot
# Most of the Matplotlib lies under the pyplot
# usually ipmported under the plt 
# Draw a line in a diagram
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 6])
y = np.array([0, 250])
plt.plot(x, y)
plt.show()

# Matplotlib Plotting
# Plotting x and y points
# x-axis is the horizontal axis(truc hoanh)
# y-axis is the vertical axis(truc tung)

# Plotting Without Line
# Draw two points in the diagram
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 8])
y = np.array([3, 10])

plt.plot(x, y, 'o')
plt.show()

# Multiple Points
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,6,8])
y = np.array([3,8,1,10])

plt.plot(x, y)
plt.show()

# Default X-Points
# If do not specify the points on the x-axis
# they will get the default values 0,1,2,3,..
# Plotting without x-points

# Markers
# Can use the keyword argument marker to emphasize
# each point with a specified marker

# Format Strings fmt
# Cu phap: marker|line|color
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, 'o:r')
plt.show()

# Marker Size
# Set the size of the markers
import matplotlib.pyplot as plt
import numpy as np

y = np.array([3, 8, 1, 10])
plt.plot(y, marker = 'o', ms = 20)
# Marker Color
# plt.plot(y, marker = 'o', ms = 20, mec = 'r')
plt.show()

# Linestyle
# Use argument linestyle or shorter ls to change the style
