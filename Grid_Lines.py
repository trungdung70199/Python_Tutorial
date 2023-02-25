# Add Grid Lines to a Plot
# Use grid()function to add grid lines to the plot
import matplotlib.pylot as plt
import numpy as np

x = x.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = y.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid()

plt.show()

