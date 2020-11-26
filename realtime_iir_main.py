from pyfirmata2 import Arduino
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IIR_filter import IIR_filter_2ndOrder
from pynput.keyboard import Key, Controller # Adds controller to keyboard

# Realtime oscilloscope at a sampling rate of 50Hz
# It displays analog channel 0.
# You can plot multiple chnannels just by instantiating
# more RealtimePlotWindow instances and registering
# callbacks from the other channels.


#PORT = Arduino.AUTODETECT
# PORT = '/dev/ttyUSB0'

# Creates a scrolling data display
class RealtimePlotWindow:

    def __init__(self):
        # create a plot window
        self.fig, self.ax = plt.subplots()
        # that's our plotbuffer
        self.plotbuffer = np.zeros(500)
        # create an empty line
        self.line, = self.ax.plot(self.plotbuffer)
        # axis
        self.ax.set_ylim(-0.05,0.05)
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
realtimePlotWindow = RealtimePlotWindow()
realtimePlotWindow2 = RealtimePlotWindow()

# sampling rate: 100Hz
samplingRate = 100

filterDC = IIR_filter_2ndOrder( 0.78429785, -1.56859571,  0.78429785, -1.76995414, 0.78402168)
filterDC2 = IIR_filter_2ndOrder(1.        , -2.        ,  1.        , -1.82269493, 0.83718165)
filterDC3 = IIR_filter_2ndOrder( 1.        , -2.        ,  1.        , -1.92188606, 0.93716115)

filterLP = IIR_filter_2ndOrder(1.11171764e-02, -1.77905018e-04,  1.11171764e-02, -1.23046251e+00,  3.91758991e-01)
filterLP2 = IIR_filter_2ndOrder(1.00000000e+00, -1.53404451e+00,  1.00000000e+00, -1.48743241e+00,  6.23734470e-01)
filterLP3 = IIR_filter_2ndOrder(1.00000000e+00, -1.73602396e+00,  1.00000000e+00, -1.75191261e+00,  8.75313200e-01)

keyboard = Controller()

# called for every new sample which has arrived from the Arduino
def callBack(data):
    
    # send the sample to the plotwindbow
    # add any filtering here:
        
    intermediate  = filterDC.dofilter(data)
    intermediate = filterDC2.dofilter(intermediate)
    output = filterDC3.dofilter(intermediate)
    
    intermediate  = filterLP.dofilter(output)
    intermediate  = filterLP2.dofilter(intermediate)
    output        = filterLP3.dofilter(intermediate)
    # data = self.myfilter.dofilter(data)
    
    if output >= 0.04:
        keyboard.press(Key.space)
        keyboard.release(Key.space)
        print("SpaceJump")
        
    realtimePlotWindow.addData(data)
    realtimePlotWindow2.addData(output)

# Get the Ardunio board.
board = Arduino('COM3')


# Set the sampling rate in the Arduino
board.samplingOn(1000 / samplingRate)

# Register the callback which adds the data to the animated plot
board.analog[3].register_callback(callBack)
# Enable the callback
board.analog[3].enable_reporting()


# show the plot and start the animation
plt.show()

# needs to be called to close the serial port
# board.exit()

print("finished")