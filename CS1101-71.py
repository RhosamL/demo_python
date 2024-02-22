"""By the end of this assignment, you will be able to perform addition, deletion, and sorting on the elements of the list as well shall be able to experiment list and related operators 

(a). Consider that you are working as Data Analyst in an organization. The HR department needs you to carry out following operation on existing list of 10 employees name (you can assume 10 names in a list here). 

Split the list into two sub-list namely subList1 and subList2, each containing 5 names. 
A new employee (assume the name “Kriti Brown”) joins, and you must add that name in subList2. 
Remove the second employee's name from subList1. 
Merge both the lists. 
Assume there is another list salaryList that stores salary of these employees. Give a rise of 4% to every employee and update the salaryList.  
Sort the SalaryList and show top 3 salaries. 
Write the Python code and output for the same. 

(b). Design a program such that it converts a sentence into wordlist. Reverse the wordlist then. Write the code and output for the same."""

names = ["Ade", "Caleb", "Jane", "Joan", "Abel", "Light", "Kate", "Kang", "Soong", "Tunde"]

# Splitting a list into sublists

#split_index = 2
subList1 = names[0 : 5]
subList2 = names[5 : ]

subList2.append("Kate Brown")
print(subList2)

subList1.pop(1)
print(subList1)

merged_list = subList1 + subList2
print(merged_list)

salary = [200, 203, 500, 400, 100, 140, 600, 500, 700, 900]

# Original salary list
salary = [200, 203, 500, 400, 100, 140, 600, 500, 700, 900]

# Update the original salary list with a 4% increase
for i in range(len(salary)):
    salary[i] *= 1.04

# Printing the updated salary list
print("Updated Salary:", salary)

# Original salary list
salary = [200, 203, 500, 400, 100, 140, 600, 500, 700, 900]

# Create a sorted copy of the salary list in descending order
sorted_salary = sorted(salary, reverse=True)

# Print the top three salaries using a loop
print("Top Three Salaries:")
for i in range(3):
    print(sorted_salary[i])
    
    
# Function to convert a sentence into a reversed word list
def reverse_wordlist(sentence):
    # Split the sentence into a list of words
    words = sentence.split()

    # Reverse the order of the words in the list
    reversed_words = words[::-1]

    return reversed_words

# Input sentence
input_sentence = "Design a program that converts a sentence into wordlist"

# Call the function to get the reversed word list
reversed_word_list = reverse_wordlist(input_sentence)

# Print the original sentence
print("Original Sentence:", input_sentence)

# Print the reversed word list
print("Reversed Word List:", reversed_word_list)
