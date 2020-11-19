import scipy.signal as sig
import matplotlib.pyplot as pyplot
import numpy as np

fs = 100
fc = 2

b,a = sig.butter(2,fc/fs*2,btype='high')
sos = sig.butter(2,fc/fs*2,btype='high',output='sos')

w,h = sig.freqz(b,a)
pyplot.plot(w/np.pi/2,20*np.log10(np.abs(h)))