import numpy as np
import matplotlib.pyplot as plt
fs=1000; t=np.arange(fs)/fs
signal=np.sin(2*np.pi*5*t)
plt.plot(t,signal); plt.xlabel('Время, с'); plt.grid(); plt.show()
