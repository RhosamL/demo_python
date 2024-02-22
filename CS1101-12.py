import math


print("Welcome to Ben store. Here is our list:")

list = ["Item 1", "Item 2", "Item 3"]
for index in range(3):
    lists = list[index]
    print(f" {lists}")

print("Special combo pack with two unique items gets a 10 percent discount \n purchase a gift pack and get a 25 percent discount")
print("How many items do you want to pick?")

def calculate_discount(total_items):
    
    if total_items == 1:
        return 0
    elif total_items == 2:
        return 0.10
    elif total_items == 3:
        return 0.25

def calculate_total_cost(item_price, quantity, discount):
 
    total_cost = item_price * quantity
    total_cost -= total_cost * discount
    return total_cost

#Example usage
item_price = 10.0
quantity = 2

# Calculate the discount based on the quantity
discount_percentage = calculate_discount(quantity)

# Calculate the total cost after applying the discount
total_cost = calculate_total_cost(item_price, quantity, discount_percentage)

# Output the results
print(f"Item Price: ${item_price}")
print(f"Quantity: {quantity}")
print(f"Discount Applied: {discount_percentage * 100}%")
print(f"Total Cost: ${total_cost}")