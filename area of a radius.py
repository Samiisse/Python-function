#alculate the area of a circle given its radius

import math

def calculate_area_of_circle(radius):
    area = math.pi* (radius**2)
    return area

radius = int(input("Enter the radius: "))
circle_area = calculate_area_of_circle(radius)

print(f"The area of a circle wuth radius {radius} is {circle_area: 2f}")