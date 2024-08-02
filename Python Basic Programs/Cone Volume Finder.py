import math

'''
Create a function that takes the height and radius of a cone as arguments and returns
the volume of the cone rounded to the nearest hundredth. See the resources tab for
the formula.
Examples
cone_volume(3, 2) ➞ 12.57
cone_volume(15, 6) ➞ 565.49
cone_volume(18, 0) ➞ 0
'''


def cone_volume(height, radius):
    volume = (1/3) * math.pi * radius**2 * height
    return round(volume, 2)

height = float(input("Enter the height of the cone: "))
radius = float(input("Enter the radius of the cone: "))

print("Volume of the cone:", cone_volume(height, radius))