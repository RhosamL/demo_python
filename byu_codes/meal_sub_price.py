
child_meal = float(input("What is the price of a child's meal: $"))
adult_meal = float(input("what is the price of an adult's meal: $"))

children = int(input("Please how many children are there: "))
adult = int(input("and the adults: "))

sub_total = (child_meal * children) + (adult_meal * adult)

print(f"Here's the subtotal: ${sub_total:.2F}")
