# Matplotlib Labels and Title
# Create Labels for a Plot
# Add labels to the x- and y-axis
import sys
import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250,  260, 270, 280, 290, 300, 310, 315, 320, 330])

plt.plot(x, y)

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

# Position the Title
# Can use the loc parameter in title() to position
# Legal values are 'left', 'right', 'center'
import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data", loc = 'left')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)
plt.show()

plt.savefig(sys.stdout.buffer)
plt.stdout.flush()

