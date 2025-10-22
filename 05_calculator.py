# Created two inputs as variables. Made sure they are set as float so no errors happen
x = float(input("Enter your first number here: "))
y = float(input("Enter your second number here: "))

# Made a list using prints. Each number are considered a value.
print()
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponents")
print("6. Floor Division")
print("7. Remainder")
print()

# Used the result as a the variable to select the string value.
result = input("What operation do you want to use? (TYPE ONLY THE NUMBER ON TOP) ")

# Now finally used if elif and else statements. Made sure the result is 100% accurate. Copy and pasted
# And modified a bit on the operations
if result == "1":
    print("Result: ")
    print(x + y)

elif result == "2":
    print("Result: ")
    print(x - y)

elif result == "3":
    print("Result: ")
    print(x * y)

elif result == "4":
    # Since you canot divide by 0 and if y == 0, made sure the new if statement is nested by the "elif" statement
    # so it would cause no error.
    if y == 0:
        print("Error: Cannot divide by 0.")
    else:
        print("Result: ")
        print(x / y)

elif result == "5":
    print("Result: ")
    print(x ** y)

elif result == "6":
    # Also made sure you cannot divide by 0 here since it is undefined.
    # check if y is zero since you cannot divide by zero
    if y == 0:
        print("Error: Cannot divide by 0.")
    else:
        print("Result: ")
        print(x // y)

elif result == "7":
    print("Result: ")
    print(x % y)

    # Made sure the else statement would be very invalid
else:
    print("INVALID OPTION!")
