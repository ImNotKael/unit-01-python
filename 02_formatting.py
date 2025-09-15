"""
TASK 1:
Write code that checks if a user entered the correct password.
The password should not be case sensitive
"""

#create a variable with an input
print()
code = input("Passcode: ")

# Use if and else statements to determine if the password would be right or wrong
if code == "Banana":
    print("Access")
else:
    print("Denied")
print()


"""
TASK 2:
Write code that checks if a user inputs an empty string
If the string is empty, print "invalid" otherwise print "valid"
"""
# Create a variable. Make sure to have .strip() to prevent any duplicates
thing = input("Enter a word: ").strip()

# Used if else statements
if thing == "":
    print("invalid")
else:
    print("valid")

"""
TASK 3:
Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 
"""

# Create two variables. the second variable must be replaced with the first one. Once done you can print the second variable
# to get the first varibale without having to print it out.
a = "cat"
b = a.replace("cat" , "dog")
print()
print(b)
print()

"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""

# Create two inputs labaled on what it should be.
name = input("Whats your name here? ")
age = input("How old are you? ")

# Print it out with strings and comas so there wouldnt be any kind of errors.
print("Hello. I am" , name , "and I am" , age , "years old")

"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""

# Create two variables
a = 1 / 3
# Use formatting method in order to round to nearest tenth.
b = f"Result {a:.1f}"


print()
print(b)
