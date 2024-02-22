import math

def print_circum(radius):
    
    circumference = 2 * math.pi * radius
    print(f"The circumference of a circle with radius {radius} is: {circumference:.5f}")

#Using the function with different radius values
print_circum(5.0)
print_circum(7.5)
print_circum(10.2)