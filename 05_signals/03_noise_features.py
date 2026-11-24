import numpy as np
rng=np.random.default_rng(42)
fs=1000; t=np.arange(fs)/fs
for f in [5,12]:
    signal=np.sin(2*np.pi*f*t)+0.5*rng.normal(size=fs)
    amp=np.abs(np.fft.rfft(signal)); freq=np.fft.rfftfreq(fs,1/fs)
    peak=freq[1+np.argmax(amp[1:])]
    print('Истинная частота:',f,'найденная:',peak,'RMS:',np.sqrt(np.mean(signal**2)))
# Это извлечение признаков, а не обученный классификатор.
