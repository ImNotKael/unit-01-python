"""
Identify the potential errors in the following code snippets and modify 
them to include appropriate try/except blocks to handle exceptions gracefully.
"""


"""
Example 1: Division
"""

print()
print("EXAMPLE 1:")
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print("Result:", result)
    except ZeroDivisionError:
        # If error occurs then print this message
        print("You cannot divide by zero. Try again")

# Example usage:
divide_numbers(10, 0)

"""
Example 2: Opening Files
"""

print()
print("EXAMPLE 2:")
def read_file(filename):
    try:
        file = open(filename, 'r')
        contents = file.read()
        print("File contents:", contents)
        file.close()
    except:
        # If no file found, prints this out.
        print("File not found. Try again")

# Example usage:
read_file("nonexistent.txt")

"""
Example 3: List Items
"""

print()
print("EXAMPLE 3")
def get_item(lst, index): 
    try:   
        item = lst[index]
        print("Item:", item)
    except:
        # If item is unknown, prints this out
        print("Item not found. Try again.")

# Example usage:
my_list = [1, 2, 3]
get_item(my_list, 5)

"""
Example 4: Dictionaries
"""

print()
print("EXAMPLE 4:")
def get_value(dictionary, key):
    try:
        value = dictionary[key]
        print("Value:", value)
    except:
        # If Value is undefined, prints this out instead.
        print("Value not found. Try again.")

# Example usage:
my_dict = {"a": 1, "b": 2}
get_value(my_dict, "c")

"""
Example 5: Else/Finally
Modify the following code to include an else block to execute code if no exceptions occur 
and a finally block to ensure that a certain action is always performed, regardless of whether an exception is raised.
"""

print()
print("EXAMPLE 5:")
def process_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:", contents)
    except FileNotFoundError:
        # If file content invalid, prints this out
        print("Error: File content not found.")
    else:
        # If it is valid and found, prints this out instead
        print("File opened successfully")
    finally:
        # This loads the file that tells the user if its complete.
        print("File load complete.")

# Example usage:
process_file("example.txt")