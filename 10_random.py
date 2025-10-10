# Made sure to import "random"
import random
"""
Task 1 (random module):
Write a program that simulates rolling a six-sided die 10 times.
Print each roll result.
"""



print()
print("TASK 1")
# Used for statement and made it a range so it prints out 6 times
# Used randint so the 6 sided die has a number of 1-6.
# Very important to use randint so it includes the last number.
for dice in range(10):
    x = random.randint(1, 6)
    print(x)

"""
Task 2 (random module):
Write a program that generates 5 random floating-point numbers between 0 and 1.
Then generate 5 random floating-point numbers between 10 and 20.
Print both sets of numbers.
"""

print()
print("TASK 2")

# Same thing as the first task, but prints out 5 different floats.
# Used the uniform fuctnion to generate the float instead of only having 0 and 1
# Same applies for from 10 to 20.
print("From 0 to 1")
for y in range(5):
    x = random.uniform(0, 1)
    print(f"{x:.2f}")
print()
print("From 10 to 20:")
for y in range(5):
    z = random.uniform(10, 20)
    print(f"{z:.2f}")


"""
Task 3 (random module):
Create a list of colors: ["red", "blue", "green", "yellow", "purple"].
Write a program that randomly selects and prints 3 colors from this list without replacement.
"""

print()
print("Task 3")

# Created a list of colors
# Made sure it printed out three times using the range
# Used the choice because the data type in the list are strings. Which cannot be used by randint or random.
Thelist = ['red' , 'orange' , 'yellow' , 'green' , 'purple']
for y in range(3):
    print(random.choice(Thelist))


"""
Task 4 (random module):
Write a program that creates a list of numbers from 1 to 10, then shuffles the list
and prints the shuffled result.
"""

# Created a list of numbers
# Printed out the original number list
numberlist = [1,2,3,4,5,6,7,8,9,10]
print()
print("Task 4")
print(numberlist)
print()
print("Shuffled list")
# Used the shuffle command to change the orders of the numbers and then printed it out
random.shuffle(numberlist)
print(numberlist)
# It will not work if you just use a random or randint in this situation because the numbers will guarantee be printed as the same one
# and would NOT be considered a shuffle and instead just a print of random numbers