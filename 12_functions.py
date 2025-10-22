"""
Task 1: Greeting
Write a function that takes a name as a 
agrument and prints a greeting message like "Hello, [name]!".
"""

print()
print("TASK 1")
"""
Used a function that prints out the greeting mentioned
"""
def hellothing(name):
    print(f"Hello {name}")

"""
Then gave the function the variable name for "name"
"""
hellothing("Kael")

# ------------------------------------------------------------

"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""

print()
print("TASK 2")
"""
Created a function that squares a number.
"""
def square(a, b):
    return a ** b

"""
Created a variable for the function with a number to be squared. Printed "x" afterwards
"""
x = square(5, 2)
print(x)

# ------------------------------------------------------------

"""
Task 3: Even or Odd
Write a function that takes a number as a argument that 
returns `True` if the number is even, and `False` otherwise.
"""

print()
print("TASK 3")
"""
Created a function that deternmines if a number is even or odd.
"""
def evenorodd(x):
    """
    Used if statement to check if the number is even or odd.
    """
    if x % 2 == 0:
        """
        Used return statement for True if even. Then False if odd.
        """
        return True
    else:
        return False
"""
Created a variable for the function with a random number to be checked. Printed "x" afterwards
"""
x = evenorodd(4)
print(x)

"""
Task 4: Area of a Rectangle
Write a function that takes the length and width of a rectangle and returns its area.
"""

# ------------------------------------------------------------

print()
print("TASK 4")
"""
Created a function to calculate length times width to get area. (length * width)
"""
def square(a, b,):
    """
    Used return statement to calculate area by multiplying length and width.
    """
    return a * b

"""
Gave a random length and width for the variable printed out with the area.
"""
x = square(4, 7)
print(x)

"""
Task 5: Celsius to Fahrenheit
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""

# ------------------------------------------------------------

print()
print("TASK 5")
"""
Created a fuunction that converts Celsius to Fahrenheit.
"""
def temp(Cel):
    """
    Used the return statement to create the formula for converting celsius to fahrenheit.
    """
    return Cel * 9/5 + 32
"""
Created a variable for a random celsius tempurate to be converted. Printed that variable.
"""
x = temp(14)
print(x)

# ------------------------------------------------------------

"""
Task 6: Average of Numbers
Write a function that takes a list of numbers as an argument
and returns the average (mean) of those numbers.
"""

print()
print("TASK 6")
"""
Created a function for calculating the average of numbers in the list below.
"""
def avg(y):
    """
    Used if statement to check if theres no numbers in the list to avoid division by zero error.
    """
    if not y:
        return 0
    """
    Used the return statement to calculate the total sum of the numbers divided by how many numbers there are in the list.
    """
    return sum(y) / len(y)
"""
Created a list of numbers to be calculated for the average. Finally printed the average.
"""
numbers = [5,2,7,5,9]
average = avg(numbers)
print(average)

# ------------------------------------------------------------

"""
Task 7: Total Calculator
Create a function that has arguments for the price and quantity of something, 
and returns the total.
"""

print()
print("TASK 7")
"""
Created a function to determine the price and quanity
"""
def totalprice(price, quantity):
    """
    Used return statement to calculate the total price by multiplying price and quantity.
    """
    return price * quantity
"""
Gave a variable for the function with a price and quantity and then printed it out.
"""
x = totalprice(24, 5)
print(f"${x}")

# ------------------------------------------------------------

"""
Your function should also optionally accept a 3rd argument for discount as a float, 
and return the discounted if provided.
"""