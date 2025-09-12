"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.

"""
a = 3.0
b = int(a)
print()
print(a)
print(b)
(print)

# Made the variable, "a" as a float variable. Then used another variable, "b" to convert the floating variable to an integer.
# Once done I print NOT the variable A, but the variable B

"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""

a = 0
print()
if a < 0:
    print("negative")
elif a > 0:
    print("positive")
else:
    print("Number is zero")
print()

# Made one variable, "a". Used if, elif, and else to determine if the variable is positive, negative, or 0.

"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""

a = 2
b = 4.0
print()
print(a + b)
print()

# Created two variables, then printed these variables adding up for the result.

"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""

Dico = {
    'orange': 1,
    'grapes': 2
}
print()
print(Dico["grapes"])
print()

# Made a dictonary with two variables, with given name and number. Then printed out the string name using the bracket so the dictonary can work

"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""
x = "1,2,3"
y = x.split(",")
print(x)
print(y)

# Created two variables. Even used the split command and printed out both results of x and y


"""
TASK 6:

Create a list of your favorite subjects (as strings). 
Use the join() function to combine all subjects into a single string separated by commas.
Then create another version using " - " as the separator.
Print both the original list and both joined strings.
"""

subjects = ["Science" , "Math" , "Computer Science"]
thing = "-".join(subjects)
print()
print(subjects)
print(thing)
print()