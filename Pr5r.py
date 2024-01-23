import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([10, 113])
y = np.array([13, 1])

plt.subplot(1, 2, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 20, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)

plt.show()
