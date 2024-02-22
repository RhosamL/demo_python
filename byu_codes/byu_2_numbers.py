#pi = 3.14159
# type conversion
radius = 7
two = 2
#print(float(two) *float(pi) / float(radius))
#print("value of pi is: " + str(pi))
number = 7
print(f"the number is {number}.")
print("Using the last variable {} in this string." .format(two))
print(f"The radus of a circle is {radius}")
#New demo to format decimals
gg = 5
hh = 7
print(gg / hh) # gave a float 0.7142857142857143
four_decimal = gg / hh
print(f"using only the four numbers of the above, {four_decimal:.4F}")
#scientific notations
earth = 1400 ** 17
print(f"earth's radius is about {earth :.4e}") #:3e oe 3e is exponent or scientific notation.

#adding commas and underscore to group long numbers
bb = 10 * 100055
print(f"\n long numbers to print {bb : ,}")
print(f"\n with underscore, {bb: _}")
print(f"\n then last without any seperation {bb}")