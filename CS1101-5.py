#Still a function. Trying to understand now.

def is_even(number):
    #Syntax is def then function name thought of simply, then parameter in bracket. Parameter is replaced when function is used.
    """Checks if the given number is even or not."""
    if number % 2 == 0:
        return True
    else:
        return False
    
#Also, this can be simplified further to be easier:

def is_odd(number1):
    """Checks whether the given number is odd or not."""
    return number1 % 2 == 1

#Then create a new function to check the above function if it works. But even without creating a new function
#we can use print() method to test our functions.

result1 = is_even(4)
print(result1)

result2 = is_odd(6)
print(result2)

#Without writing true or false, terminal gave fasle for the second statement, so there was need to specify if something happens true.
word = 'bAnana'

index = word.find('a')

print(index)

n = 10
while n != 1:
    print(n,)
    if n % 2 == 0: # n is even
        n = n / 2
    else: # n is odd
        n = n * 3 + 1