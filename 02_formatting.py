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
# Create a variable 
thing = input("Enter a word: ").strip()

if thing == "":
    print("invalid")
else:
    print("valid")

"""
TASK 3:
Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 
"""

a = "cat"
b = a.replace("cat" , "dog")
print()
print(b)

"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""


"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""