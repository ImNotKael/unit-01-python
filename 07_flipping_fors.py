"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""

# Created a variable and used the for statement so it prints out an individual letter.
letters = "hi my name is kael"
print()
print("TASK 1")
for x in letters:
    print(x)
print()

"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""

# Created two variahles. The sum as x and the numbers shown "numbers"
numbers = [1,2,3,4,5]
x = 0
print()
print("TASK 2")
# Used for statement in numbers where it adds by num
for num in numbers:
    x += num
print(x)
print()

"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""

# Created a variable and list that shows that variable. Then printed it out
la = "Everything shall end"
list(la)
print()
print("TASK 3")
for x in la:
    print(x)
print()



"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result



In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""

# Printed a variable with a string and a number 
print()
print("TASK 4")
dictionary = {
    "Soccer": 4 ,
    "basketball": 1 ,
    "Baseball": 4,
    "Tennis": 0,
}

# When printing out from the for statement, made sure to add an index because the dictionary used works exactly like an index
# so it prints out only numbers.
for x in dictionary:
    print(dictionary[x])
