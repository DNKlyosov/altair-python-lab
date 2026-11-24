import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
plt.plot(x, x**2, label='y = x²')
plt.xlabel('x'); plt.ylabel('y'); plt.legend(); plt.grid()
plt.show()
