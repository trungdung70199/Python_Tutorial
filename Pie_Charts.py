# Matplotlib Pie Charts
# Creating Pie Charts
# Use the pie() function to draw pie charts
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show()

# Labels 
# Add labels to the pie chart with label parameter
# A simple pie chart
# Start Angle: Can choose the start angle
# Use startangle parameter
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
# plt.pie(y, labels = mylabels, startangle = 90)
plt.show()

# Explode
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.1, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show()

# Sadow
# Add a shadow to the pie chart by setting the sadows parameter
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show() 

# Color 
# 'r' - Red
# 'g' - Green
# 'b' - Blue
# 'c' - Cyan
# 'm' - Magenta
# 'y' - Yellow
# 'k' - Black
# 'w' - White

# Legend function
#  Legend With Header
# Add the title parameter to the legend function

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
# plt.legend()
plt.legend(title = "Four Fruits:")
plt.show()
