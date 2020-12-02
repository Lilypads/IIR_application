from pyfirmata2 import Arduino
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IIR_filter import IIRFilter
from pynput.keyboard import Key, Controller # Add keyboard controller
import scipy.signal as sig

# Realtime oscilloscope at a sampling rate of 50Hz
# It displays analog channel 0.
# You can plot multiple chnannels just by instantiating
# more RealtimePlotWindow instances and registering
# callbacks from the other channels.


#PORT = Arduino.AUTODETECT
# PORT = '/dev/ttyUSB0'

# Creates a scrolling data display
class RealtimePlotWindow:

    def __init__(self, ylim1,ylim2):
        # create a plot window
        self.fig, self.ax = plt.subplots()
        # that's our plotbuffer
        self.plotbuffer = np.zeros(500)
        # create an empty line
        self.line, = self.ax.plot(self.plotbuffer)
        # axis
        self.ax.set_ylim(ylim1,ylim2)
        # That's our ringbuffer which accumluates the samples
        # It's emptied every time when the plot window below
        # does a repaint
        self.ringbuffer = []
        # add any initialisation code here (filters etc)
        # start the animation
        self.ani = animation.FuncAnimation(self.fig, self.update, interval=100)

    # updates the plot
    def update(self, data):
        # add new data to the buffer
        self.plotbuffer = np.append(self.plotbuffer, self.ringbuffer)
        # only keep the 500 newest ones and discard the old ones
        self.plotbuffer = self.plotbuffer[-500:]
        self.ringbuffer = []
        # set the new 500 points of channel 9
        self.line.set_ydata(self.plotbuffer)
        return self.line,

    # appends data to the ringbuffer
    def addData(self, v):
        self.ringbuffer.append(v)


# Create an instance of an animated scrolling window
# To plot more channels just create more instances and add callback handlers below
realtimePlotWindow = RealtimePlotWindow(0.35,0.45)
realtimePlotWindow2 = RealtimePlotWindow(-0.05,0.05)

# sampling rate: 100Hz
samplingRate = 100

# DC line filter
fc = 2      # cutoff frequency
sosDC = sig.butter(6,fc/samplingRate*2,btype='high',output='sos')

# deleting high frequency noise
fc = 8      # cutoff frequency
sosLP = sig.cheby2(6,40,fc/samplingRate*2,btype='low',output='sos')

# instantiate the 2nd order chain class
filterDC = IIRFilter(sosDC)
filterLP = IIRFilter(sosLP)

# # instantiate the iir filter with coefficients
# filterDC = IIR_filter_2ndOrder(0.78429785, -1.56859571, 0.78429785, -1.76995414, 0.78402168)
# filterDC2 = IIR_filter_2ndOrder(1.        , -2.        , 1.        , -1.82269493, 0.83718165)
# filterDC3 = IIR_filter_2ndOrder(1.        , -2.        , 1.        , -1.92188606, 0.93716115)

# filterLP = IIR_filter_2ndOrder(1.11171764e-02, -1.77905018e-04, 1.11171764e-02, -1.23046251e+00, 3.91758991e-01)
# filterLP2 = IIR_filter_2ndOrder(1.00000000e+00, -1.53404451e+00, 1.00000000e+00, -1.48743241e+00, 6.23734470e-01)
# filterLP3 = IIR_filter_2ndOrder(1.00000000e+00, -1.73602396e+00, 1.00000000e+00, -1.75191261e+00, 8.75313200e-01)

# instantiate keyboard controller
keyboard = Controller()

# called for every new sample which has arrived from the Arduino
def callBack(data):
    
    # send the sample to the plotwindbow
    # add any filtering here:
        # data = self.myfilter.dofilter(data)
     
    output = filterDC.dofilter(data) 
    output = filterLP.dofilter(output)
    
    # intermediate = filterDC.dofilter(data)
    # intermediate = filterDC2.dofilter(intermediate)
    # output = filterDC3.dofilter(intermediate)
    
    # intermediate  = filterLP.dofilter(output)           # comment these 3 out for DC filter only
    # intermediate  = filterLP2.dofilter(intermediate)    # comment these 3 out for DC filter only
    # output        = filterLP3.dofilter(intermediate)    # comment these 3 out for DC filter only
    
    # jump
    if output >= 0.04:
        keyboard.press(Key.space)
        keyboard.release(Key.space)
        #print("SpaceJump")
        
    realtimePlotWindow.addData(data,)
    realtimePlotWindow2.addData(output)

# Get the Ardunio board.
board = Arduino('COM3')


# Set the sampling rate in the Arduino
board.samplingOn(1000 / samplingRate)

# Register the callback which adds the data to the animated plot
board.analog[3].register_callback(callBack)         # analog pin a3 of Arduino connects to z-axis of the sensor
# Enable the callback
board.analog[3].enable_reporting()


# show the plot and start the animation
plt.show()

# needs to be called to close the serial port
# board.exit()

print("finished")