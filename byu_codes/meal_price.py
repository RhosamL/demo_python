#Additional features: Made the display more interactive
#added currency to the input values
#used a new function (round ()2) to display a float in 2 decimals

child_meal = float(input("What is the price of a child's meal: $"))
adult_meal = float(input("what is the price of an adult's meal: $"))

children = int(input("Please how many children are there: "))
adult = int(input("and the adults: "))

sub_total = (child_meal * children) + (adult_meal * adult)

print(f"Here's the subtotal: ${sub_total:.2F}")

tax = float(input("what is your sales tax rate - please enter a number with no decimals: "))
sales_taxes = sub_total * (tax / 100)
print (f"your total after taxes is ${sales_taxes:.2F}")

total = sub_total + sales_taxes
print ("Your final bill will be $", round((total),2))

bill = int(input("How much bill are you bringing?: $"))
print("please wiat for your change...\n")
change = bill - total
print(f"your change is ${change:.2F}. Thank you")