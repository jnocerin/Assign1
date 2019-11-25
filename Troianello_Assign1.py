# FE 595 Assignment 1
# Author: Jessica Nocerino Troianello
# Team Members: Brooke Crowe, Colin Stipcak, Gordon Garisch, Jessica Troianello

# Import Libraries
import numpy
import matplotlib.pyplot as plt

def plotSinCos(x):
    # Readout of Random Values Generated
    print("the values of X are " + str(x))
    # Sort values of X
    #x=sorted(x)

    # Plot Sine and CoSine
    plt.plot(x, numpy.sin(x))
    plt.plot(x, numpy.cos(x))
    plt.plot(x, numpy.tan(x))  # Added by Gordon Garisch
    plt.title ("Plot of Sine CoSine and Tangent")
    plt.legend(("Sine", "Cosine", "Tangent" ))
    plt.show()

# Generate 360 random numbers between 0 and Pi*2
#x = numpy.random.uniform(low=0, high=(numpy.pi * 2), size=(360))
#x1 = numpy.arange(start=0, stop=(numpy.pi*2), size=360)
xInput = numpy.linspace(start=0, stop=(numpy.pi*2), num=360)

plotSinCos(xInput)