# FE 595 Assignment 1
# Author: Jessica Nocerino Troianello
# Team Members: Brooke Crowe, Colin Stipcak, Gordon Garisch, Jessica Troianello

#Import Libraries
import numpy
import matplotlib.pyplot as plt

#Generate 360 random numbers between 0 and Pi*2
x = numpy.random.uniform(low=0, high=(numpy.pi*2), size=(360))

#Readout of Random Values Generated
print ("the values of X are "+ str(x))

#Plot Sine and CoSine
plt.plot(x,numpy.sin(x))
plt.plot(x,numpy.cos(x))
plt.show()