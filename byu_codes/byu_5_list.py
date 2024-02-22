#Collections in python -- list is the most common.
#list = [1,2,3,"hello","world"] List [list]

clients = [] #shorthand way to write [] is list()

new_clients = ""

while new_clients != "end":
    new_clients = input("What is the name of your student: ")
    rnew_client = new_clients.lower()
    
    if new_clients != "end":
        clients.append(new_clients)
    else:
        print ("No more students")

for client in clients:
    print(client)

x = 5
x += 1
print(x)
my_list= [3, 5, 7, 2, 5, 3, 6]
smallest = 100

for value in my_list:

    if value < smallest:

        smallest = value

print(f"The smallest is {smallest}")
#tips = [2, 56, 79, 98.7, 56]
#run_total = 0
#for tip in tips:
#    run_total = run_total + tip #shorthand way -- +=
#It takes the value of run_total, back up, and uses it again.
#print(run_total)
