'''
Andrew Cohen
'''
import math

def CircleArea(diameter):

    radius = .5 * diameter

    area = radius * math.pi
    return area

def ShowCircleArea(diameter):

    diameter = float(input("what is the diameter"))
    # the area is radius (square) * pie
    # let us calculate radius:

    # radius = .5 * diameter
    #
    #
    # area = radius * math.pi
    # return area

    #print("The area of a circle of {0}".format(diameter),"is {0}".format(area))

