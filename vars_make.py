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

# Processing
# Area
area_circle = (radius_of_circle**2) * math.pi
area_rectangle = length_of_rectangle*width_of_rectangle
area_octagon = 2 * (side_length_octagon**2) * (1+math.sqrt(2))

#Perimeter
perimeter_circle = (radius_of_circle * 2 * math.pi)
perimeter_rectangle = (length_of_rectangle * 2) + (width_of_rectangle * 2)
perimeter_octagon = (side_length_octagon * 8)

# Output.
print(f"The circle has an area of {area_circle} and a perimeter of {perimeter_circle}")
print(f"The rectangle has an area of {area_rectangle} and a perimeter of {perimeter_rectangle}")
print(f"The octagon has an area of {area_octagon} and a perimeter of {perimeter_octagon}")