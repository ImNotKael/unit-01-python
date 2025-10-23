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
        print("Index not found in list. Try again")

# Example usage:
    my_list = [1, 2, 3]
    get_item(my_list, 5)

"""
Example 4: Dictionaries
"""

print()
print("EXAMPLE 4:")
def get_value(dictionary, key):
    value = dictionary[key]
    print("Value:", value)

# Example usage:
my_dict = {"a": 1, "b": 2}
get_value(my_dict, "c")


