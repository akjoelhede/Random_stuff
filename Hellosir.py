import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1,100)

print(x)

def function(x):
	return np.sin(x)

plt.plot(x, function(x))
plt.show()

ajdhsa