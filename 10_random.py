# Made sure to import randoms
import random
"""
Task 1 (random module):
Write a program that simulates rolling a six-sided die 10 times.
Print each roll result.
"""



print()
print("TASK 1")
for dice in range(10):
    x = random.randint(1, 10)
    print(x)

"""
Task 2 (random module):
Write a program that generates 5 random floating-point numbers between 0 and 1.
Then generate 5 random floating-point numbers between 10 and 20.
Print both sets of numbers.
"""

x = random.randint(0, 1)

print()
print("TASK 2")

print("From 0 to 1")
for y in range(5):
    roll = random.uniform(0, 1)
    print(f"{roll:.2f}")
print()
print("From 10 to 20:")
for y in range(5):
    roll = random.uniform(10, 20)
    print(f"{roll:.2f}")


"""
Task 3 (random module):
Create a list of colors: ["red", "blue", "green", "yellow", "purple"].
Write a program that randomly selects and prints 3 colors from this list without replacement.
"""

print()
print("Task 3")

Thelist = ['red' , 'orange' , 'yellow' , 'green' , 'purple']
for y in range(3):
    print(random.choice(Thelist))


"""
Task 4 (random module):
Write a program that creates a list of numbers from 1 to 10, then shuffles the list
and prints the shuffled result.
"""

numberlist = [1,2,3,4,5,6,7,8,9,10]
print()
print("Task 4")
print(numberlist)
print()
print("Shuffled list")
random.shuffle(numberlist)
print(numberlist)