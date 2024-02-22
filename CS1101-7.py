"""Sixth or seventh week of code. Use the terms "equivalent" and "identical" to distinguish between objects and values. Illustrate the difference further using your own examples with Python lists and the “is” operator.  

Using your own Python list examples, explain how objects, references, and aliasing relate to one another.

Finally, create your own example of a function that modifies a list passed in as an argument. Hence, describe what your function does in terms of arguments, parameters, objects, and references."""

#The term equivilent objects as used in Python is when an object has the same content or list in comparison with another. For instance, cond=sider this example;

position = [1, 2, 3, 4, 5]
# Here, the variable, position shows the first numbers up to five.

count = [1, 2, 3, 4, 5]
#In equivilent, the two variables contain the same type and quantiy and so they are equivilent. That is:
position == count

#For two variables to be identical, there have to have the same name and hld the same objects in either list form or otherwise

letters = ['x, y, z']
letters1 = letters

"""PART TWO OF ASSIGNMENT"""

items = ["Spinach", "Apple", "Gauva", "Onions", "Tomato"]