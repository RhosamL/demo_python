#Creativity: used 'end= " " option to concatenate two print statements.
# Used .append() and .pop() to add and remove items in lists
#Used the len function inside the range() function
print("Welcome to plamazon shopping")

options = ["Add item", "View cart", "Remove item", "Compute Total", "Quit"]

selection = " " #input("Please enter a number from the list above: ")
product_list = []
product_cost = []
totall = 0
while selection != '5':
    
    for i in range(len(options)):
        option = options[i]
        print(f"{i + 1}.", end= "")
        print(f" {option}")

    selection = input("Please enter a number from the list above: ")

    if selection == '1':
        product_name = input("Enter the name of the product you want to add: ")
        gproduct_cost = float(input("Enter the cost (in dollars) of the product: "))

        product_cost.append(gproduct_cost)
        product_list.append(product_name)

        print(f"{product_name} has been added")

    elif selection == '2':
        print("Your current cart is with:")

        for j in range(len(product_list)):
            jj = j + 1
            product = product_list[j]
            cost = product_cost[j]

            print(jj, end=". ")
            print(f"{product}", end= " ")
            print(f"-- Cost: ${cost:.2F}")


#        for h in range(len(product_cost)):
#            cost = product_cost[h]

#            print(f"Cost: ${cost}")

    elif selection == '3':
        remove_item = int(input("Which item would you like to remove? Please enter its position in the list: "))

        if remove_item == 1:
            product_list.pop(0)
            product_cost.pop(0)
        elif remove_item == len(product_list):
            product_list.pop()
            product_cost.pop()
        elif remove_item > len(product_list):
            print("Wrong Selection. Please try again")
        else:
            remove_item -= 1
            product_list.pop(remove_item)
            product_cost.pop(remove_item)
# Normal pop to remove all other inputs, except the firsr and second
        print(f"You have sucessfully removed the last item, your cart is: ")


    elif selection == '4':
        for add in range(len(product_cost)):
            totall += product_cost[add]
# product[add] will loop through all the product_cost items and add to totall
        print(f"The total cost of all items in your cart is ${totall:.2F} Please proceed to the checkout button")


    elif selection == '5':
        print("Thank you for using our service")

    else:
        print("Invalid Selection! Try again.")