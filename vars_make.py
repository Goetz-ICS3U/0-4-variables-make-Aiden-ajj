"""Header Comments
author: Aiden 
date: Feburary 12 2026
Make Variables
""" 

#Input
radius_of_circle = int(input("Please enter the Radius of the Circle: "))
length_of_rectangle = int(input("Please enter length of the Rectangle: "))
width_of_rectangle = int(input("Please enter the Width of the Rectangle: "))
side_length_octagon = int(input("Please enter the Side Length of the Octagon: "))

# Import
import math
pie = math.pi
s = math.sqrt

# Processing
# Area
area_circle = (radius_of_circle**2) * pie
area_rectangle = (length_of_rectangle*width_of_rectangle)
area_octagon = 2 * (side_length_octagon**2) * (1+s(2))

#Perimeter
perimeter_circle = (radius_of_circle * 2 * pie)
perimeter_rectangle = (length_of_rectangle * 2) + (width_of_rectangle * 2)
perimeter_octagon = (side_length_octagon * 8)

# Output.
print(f"The Circle has an Area of {area_circle} and a Perimeter of {perimeter_circle}")
print(f"The Rectangle has an Area of {area_rectangle} and a Perimeter of {perimeter_rectangle}")
print(f"The Octagon has an Area of {area_octagon} and a Perimeter of {perimeter_octagon}")