# Matlotlib 
# Linestyle
# Use a dotted line
import matplotlib.pyplot as plt
import numpy as np

y = np.array([1, 3, 8, 10])
plt.plot(y, linestyle = 'dotted')
plt.show()

# Shorter Syntax
# linstyle can be written ls
# dotted can be written :
# dashed can be written --
import matplotlib.pyplot as plt
import numpy as np

y = ([3, 8, 1, 10])
plt.plot(y, linestyle = '--')
plt.show()

# Line Color
# Use the keyword argument color or shorter c to set the color
import matplotlib.pyplot as plt
import numpy as np

y = ([3, 1, 8, 10])
plt.plot(y, color = 'r')
plt.show()

# Line Width
# Use linewidth or lw to change the wiidth of the line
import matplotlib.pyplot as plt
import numpy as np

y = ([1, 4, 5, 10])
plt.plot(y, linewidth = '20')
plt.show()

# Multiple Lines
# Adding more plt.plot() functions
import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 10])

plt.plot(y1)
plt.plot(y2)

plt.show()
