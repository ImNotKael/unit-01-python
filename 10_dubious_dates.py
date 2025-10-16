# imported datetime module
from datetime import datetime
"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""

# Created a variable for the current date and time
# Then printed it out.
my_date = datetime.today()
print("TASK 1")
print(my_date)

"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""

# Created a variable for the current date and time. Then used strftime to format the date into a better and easier to read format.
# Afterwards printed the formatted date.
my_date = datetime.today()
my_string = my_date.strftime("%m/%d/%Y , %X")
print()
print("TASK 2")
print(my_string)


"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""

# Created two random date strings and a date format. Then used strptime to convert the strings into dates.
# Created a variable to find the difference between the two dates and printed the difference in days.
# Created a difference variable to find the difference between the two dates and printed the difference in days.
# Printed out using format tool to make it easier to input the variables.
date_string1 = "2023-03-24"
date_string2 = "2024-11-19"
date_format = "%Y-%m-%d"
date1 = datetime.strptime(date_string1, date_format)
date2 = datetime.strptime(date_string2, date_format)
difference = date2 - date1
print()
print("TASK 3")
# Made sure to use difference.days to only get the days so it shows the difference in days only.
print(f"The difference between {date_string1} and {date_string2} is {difference.days} days.")

"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""

# Created an input for the user to enter their birthdate. Then used strptime to convert the string into a date.
# Created "today" as a variable to get the current date.
# Created an age variable to calculate the age by subtracting the birth year from the current year.
# Afterwards printed the age using an f-string for the conclusion.
print()
print("TASK 4")
birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_input, "%Y-%m-%d")
today = datetime.today()
# Used a conditional statement to check if the current month and day is before the birth month and day.
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
print()
print(f"Your age: {age} years old.")