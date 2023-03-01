# Add Grid Lines to a Plot
# Use grid()function to add grid lines to the plot
# import sys
# import matplotlib
# matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

x = x.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = y.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid()
# Only x-axis: plt.grid(axis='x')
# Only y-axis: plt.grid(axis='y')
# Color: plt.grid(color='green', linestyle='--', linewidth=0.5)

plt.show()

plt.save(sys.stdout.buffer)
sys.stdout.flush()


