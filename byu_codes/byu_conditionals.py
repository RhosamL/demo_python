#understanding if,  else, elif
#country = input("Input your Country: ")
#if country.lower() == 'usa':
#    print("home alone")
#else:
#    print("dobberman")
#An example

#price = input("How much is your total?: ")
#pprice = float(price)

#if pprice >= 1:
#    print('You have to pay $20')
#else:
#    print("you can just pay $1 and go")


#Nesting
country = input("Your country: ")
rcountry = country.lower()
state = input("your state plese: ")
rstate = state.lower()
if rcountry == 'nigeria':
    if rstate in('lagos', 'abuja', 'kano'):
        tax = 0.05
    elif rstate == 'cross river' or 'jos':
        tax = 0.03
    elif rstate in('enugu, ebonyi, aba'):
        tax = 0.04
    print(tax)
else:
    tax = 0.7    
    print(tax)