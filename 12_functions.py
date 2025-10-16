"""
Task 1: Greeting
Write a function that takes a name as a 
agrument and prints a greeting message like "Hello, [name]!".
"""

print()
print("TASK 1")
def hellothing(name):
    print(f"Hello {name}")

hellothing("Kael")

"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""

print()
print("TASK 2")
def square(a, b):
    return a ** b

x = square(5, 2)
print(x)


"""
Task 3: Even or Odd
Write a function that takes a number as a argument that 
returns `True` if the number is even, and `False` otherwise.
"""

print()
print("TASK 3")
def evenorodd(x):
    if x % 2 == 0:
        return True
    else:
        return False
x = evenorodd(4)
print(x)

"""
Task 4: Area of a Rectangle
Write a function that takes the length and width of a rectangle and returns its area.
"""

print()
print("TASK 4")
def square(a, b, c):
    return a * b * c

x = square(4, 7, 3)
print(x)

"""
Task 5: Celsius to Fahrenheit
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""

print()
print("TASK 5")
def temp(Cel):
    return Cel * 9/5 + 32
x = temp(14)
print(x)

"""
Task 6: Average of Numbers
Write a function that takes a list of numbers as an argument
and returns the average (mean) of those numbers.
"""

print()
print("TASK 6")
def avg(y):
    if not y:
        return 0
    return sum(y) / len(y)
numbers = [5,2,7,5,9]
average = avg(numbers)
print(average)

"""
Task 7: Total Calculator
Create a function that has arguments for the price and quantity of something, 
and returns the total.
"""

print()
print("TASK 7")
def totalprice(price, quantity):
    return price * quantity
x = totalprice(24, 5)
print(f"${x}")

"""
Your function should also optionally accept a 3rd argument for discount as a float, 
and return the discounted if provided.
"""