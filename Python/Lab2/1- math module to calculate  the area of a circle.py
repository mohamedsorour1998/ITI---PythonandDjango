# 1 - Write a Python program that uses the math module to calculate
# the area of a circle with a radius of 5.
import math


def mathModuleToCalculateTheAreaOfACircle(radius):
    area = math.pow(radius, 2) * math.pi
    return area


print(mathModuleToCalculateTheAreaOfACircle(5))