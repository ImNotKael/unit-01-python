'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''
# Create a variable. Then print out whether 
x = 12
print()
print("EXERCISE 1")
print(x > 10)
print()

'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''

# Created two variables. both being used an input
yesorno = input("Are you a student? ")
age = int(input("how old are you: "))

# Used if else statements to determine if the student is valid or not to only have the price of $10
if age < 18 or yesorno == 'yes':
    print("Price is only $10 since you are a student!")
    print()
else:
    print("Price is $20 since you are an adult")
    print()

'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''

# Created a variable input for fruit and a list for fruitlist
fruit = str(input("Enter a fruit name: "))
fruitlist = ["apple", "orange", "banana", "grape"]

# Used the if or else including the in statement inside
if fruit in fruitlist:
    print("Yes, that fruit is in the list.")
else:
    print("No, that fruit is not in the list.")


'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''
# Created four variables. Two as inputs and two as 
weight = int(input("Weight?: "))
Zone = str(input("What zone will you take?: "))
A = 5
B = 7

# Used if and else statements for the input values
if weight <= 0:
    print("Error: no number count.")

if Zone == "A" or Zone == "Zone A":
    weight * A
    print(weight * A)
elif Zone == "B" or Zone == "zone B":
    weight * B
    print(weight * B)
else:
    print("Select a zone")

'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''