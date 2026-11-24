import numpy as np
import matplotlib.pyplot as plt
fs=1000; t=np.arange(fs)/fs
signal=np.sin(2*np.pi*5*t)+0.5*np.sin(2*np.pi*12*t)
freq=np.fft.rfftfreq(len(signal),1/fs)
amp=np.abs(np.fft.rfft(signal))/len(signal)
amp[1:-1]*=2  # для чётного числа отсчётов: не удваиваем DC и Найквист
print('Два максимума:',freq[np.argsort(amp)[-2:]])
fig,ax=plt.subplots(2,1)
ax[0].plot(t,signal); ax[0].set_xlabel('Время, с')
ax[1].plot(freq,amp); ax[1].set_xlim(0,50); ax[1].set_xlabel('Частота, Гц')
plt.tight_layout(); plt.show()
