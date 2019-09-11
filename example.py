import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
print(x)
y = x*x*x + 1

plt.plot(x, y)
plt.show()
