# Create Bars
# Draw 4 bars
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y)
plt.show()

# The bar() function takes arguments
# Bar Width use width = size in plt.bar(x, y, width = 0.1)
import matplotlib.pyplot as plt
import numpy as np

x = ["Apple", "Banana"]
y = [400, 500]

plt.bar(x, y, width = 0.1)
plt.show()

# Horizontal Bars
# Bar Color: use color="red" in plt.bar(x, y, color = "red")
# Draw 4 horizontal bars
import matplotlib.pyplot as plt
import numpy as np

x = (["A", "B", "C", "D"])
y = ([3, 8, 1, 10])

plt.barh(x, y, color = "red")
plt.show()

# Create Histogram
import numpy as np
x = np.random.normal(170, 10, 250)
print(x)

# The hist() function will read the array and produce a histogram
# A simple histogram
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()
