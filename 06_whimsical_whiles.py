"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""

# Created variable which equals to 0
x = 0
print()
print("TASK 1")
# Created while statement and made sure x adds up by 1 first (STOPS AT 10 SINCE X < 10.)
while x < 10:
    x += 1
    print(x)
print()

"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""

# Created variable which equals to 10
x = 10
print()
print("TASK 2")
# Created a while statement which is different because it counts down instead and makes sure it doesnt get to 0.
# Used subtraction operation instead of addition so it decends.
while x > 0:
    print(x)
    x -= 1
print()


"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""

# Created two variables
x = int( input("Put your number here: "))
y = 1
print()
print("TASK 3")
# Used a while statement. made sure it is less than 0 so it would be true
# Made sure x multiplies by y so it makes a factorial
while x > 0:
    y = x * y
    x -= 1
print(y)


"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
# Created two variables, one being input and the other being the password
code = input("Whats the password? ")
password = "123"
print()
print("TASK 4")
# While statement here is similar to an if statement. The only difference here is that it is constantly looping instead of the if statement.
# the code inside the while statement will overwrite the one thats not in the while statement.
while code != password:
    print("wrong")
    code = input("Whats the password? ")
else:
    print("you are correct!")


"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""