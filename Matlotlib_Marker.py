import matplotlib.pyplot as plt
import numpy as np

y = np.array([3, 1, 4, 6, 10])
plt.plot(y, marker = 'o')
# plt.plot(y, marker = '*')
plt.show()

# Set the FACE color 
import matplotlib.pyplot as plt
import numpy as np

y = np.array([3, 8, 1, 10])
plt.plot(y, marker = 'o', ms = 20, mfc = 'r')
# plt.plot(y, marker = 'o', ms = 20, mec = 'g', mfc = 'r')
plt.show()
