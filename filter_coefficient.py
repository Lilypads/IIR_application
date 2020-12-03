import scipy.signal as sig
import matplotlib.pyplot as pyplot
import numpy as np

fs = 100    # sampling frequency
fc = 2      # cutoff frequency

# DC line filter
b,a = sig.butter(6,fc/fs*2,btype='high')
sos = sig.butter(6,fc/fs*2,btype='high',output='sos')

w,h = sig.freqz(b,a)
pyplot.figure(1)
pyplot.plot(w/np.pi/2,20*np.log10(np.abs(h)))
pyplot.title('Frequency Response DC')
pyplot.xlabel('Normalised Frequency')
pyplot.ylabel('Amplitude')

# deleting high frequency noise
fc = 8      # cutoff frequency
b,a = sig.cheby2(6,40,fc/fs*2,btype='low')
sos = sig.cheby2(6,40,fc/fs*2,btype='low',output='sos')

w,h = sig.freqz(b,a)
pyplot.figure(2)
pyplot.plot(w/np.pi/2,20*np.log10(np.abs(h)))
pyplot.title('Frequency Response High Frequency Noise')
pyplot.xlabel('Normalised Frequency')
pyplot.ylabel('Amplitude')
