from datetime import datetime
"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""

my_date = datetime.today()
print("TASK 1")
print(my_date)

"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""

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

date_string1 = "2023-01-15"
date_string2 = "2024-06-10" 
date_format = "%Y-%m-%d"
date1 = datetime.strptime(date_string1, date_format)
date2 = datetime.strptime(date_string2, date_format)
difference = date2 - date1
print()
print("TASK 3")
print(f"The difference between {date_string1} and {date_string2} is {difference.days} days.")

"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""