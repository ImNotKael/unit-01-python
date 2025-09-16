"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""

# Created variable, then printed out that variable
list = ["Fire" , "Water" , "Earth" , "Wind"]
print()
print("TASK 1")
print(list)
print()

"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""

# Created a list with nothing in it.
list = []
# Added a string on that list. Then printed out that first list
list.append("gravity")
print()
print("TASK 2")
print(list)
# Added another string on the end of the list by doing .append . Then printed it out
list.append("lightning")
print(list)
print()

"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""

# Created a new list then printed out.
list = ["fire" , "water"]
print()
print("TASK 3")
print(list)
# Used .remove and erased water to only print out fire.
list.remove("water")
print(list)
print()

"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""

# Created a new list, then printed it out
list = ["Samsung" , "Apple" , "Microsoft"]
print()
print("TASK 4")
print(list)
# Printed the same variable, but instead added [1], which only focus on index 1, which is "Apple"
print(list[1])

"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""

# Created a new list. Added an append, then printed it out.
list = []
list.append("Pen")
print()
print("TASK 5")
print(list)
# Created two different appends, then printed out the new result.
list.append("Pencil")
list.append("Eraser")
print(list)
print()

"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""

# Created a list with three indexes
list = ["samsung" , "apple" , "microsoft"]
print()
print("TASK 6")
print(list)
# Used the del function and deleted index 1, which is "apple". Printed out the new result
del list[1]
print(list)

"""
Task 7: Slicing lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""

# Created a list with four types of indexes. Then printed it out
list = ["red" , "orange" , "yellow" , "green"]
print()
print("TASK 7")
print(list)
# Printed out the variable "list" again, but instead, added a subset.
print(list[1:3])

"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""

# Created two lists, list and list2. Then printed both lists out
list = ["mrforlenza" , "carlos"]
list2 = ["msakhter" , "mrq" , "msmaria"]
print()
print("TASK 8")
print(list)
print(list2)
# Combined both lists, then printed the result one of huge list
print(list + list2)