#Determine whether to loan money or not.

loan_amount = int(input("How large is the amount you want to loan in figures, from a 1-10?: "))
credit_history = int(input("What is your credit rating on a scale of one to ten?: "))
income = int(input("What is your income? (in the number of digits): "))
down_payment = int(input("How large is your down payment(in a how many digit scale): "))

if loan_amount >= 5:
    if credit_history >= 7 and income >= 7 and down_payment >= 1:
        decision = True
    if credit_history >= 7 or income >= 7:
        if down_payment >= 5:
            decision = True
        else:
            decision = False
    else:
        decision = False

elif loan_amount <= 5:
    if credit_history < 4:
        decision = False
    elif income >= 7 or down_payment >= 7:
        decision = True
    elif income >= 4 and down_payment >= 4:
        decision = True
    else:
        decision = False

if decision:
    print("Congratulations, you can visit any of our branch to submit your documents")
if not decision:
    print("apologies, you are not qualified for a loan. please endevour to talk with a consultant")