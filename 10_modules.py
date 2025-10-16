import os
import os.path
import sys
"""
Task 1 (os module):
Write a Python program that prints the current folder (working directory) using the os module.
"""

# Created a variable to get the current working directory and printed it out.
print("TASK 1")
current_directory = os.getcwd()
print(current_directory)


"""
Task 2 (os module):
Create a new directory called "test_folder" in the current directory.
Then print a list of all files and directories in the current directory.
"""

# Created a variable for the new directory name "test_folder".
# Used an if statement to check if the directory already exists. If it doesn't exist, it creates it.
# Then created a variable to list all files and directories in the current directory and printed them out.
# Used a for loop to print each item in the list on a new line from creating "all_items".
print()
print("TASK 2")
new_directory = "test_folder"
if not os.path.exists(new_directory):
    os.makedirs(new_directory)
    print(f"Directory '{new_directory}' created.")
else:
    print(f"Directory '{new_directory}' already exists.")
all_items = os.listdir('.')
print("Files and directories in the current directory:")
for item in all_items:
    print(item)

"""
Task 3 (os module):
Write a program that checks if a directory called "data" exists in the current 
working directory. If it doesn't exist, create it. If it does exist, print 
"Directory already exists."
"""

# Created a variable for the date directory name as "data".
# Used an if statement to check if the directory already exists. If it doesn't exist, it creates it.
print()
print("TASK 3")
data_directory = "data"
if not os.path.exists(data_directory):
    os.makedirs(data_directory)
    print(f"Directory '{data_directory}' created.")
else:
    print("Directory already exists.")

"""
Task 4 (os.path module):
Write a program that checks if a file called "config.txt" exists in the current directory.
If it exists, print its path. If it doesn't exist, print "File not found."
"""

# Created file_name as a variable for "config.txt".
# Used an if statement to check if the file exists using os.path.isfile.
print()
print("TASK 4")
file_name = "config.txt"
if os.path.isfile(file_name):
    file_path = os.path.abspath(file_name)
    print(f"File path: {file_path}")
else:
    print("File not found.")

"""
Task 5 (sys module):
Write a program that prints the Python version you are currently using.
"""

# Created a python version variable to get the current Python version and printed it out.
# Shows us what version of Python we are using.
print()
print("TASK 5")
python_version = sys.version
print(f"Python version: {python_version}")

"""
Task 6 (sys module):
Write a program that prints the platform your Python interpreter is running on
(e.g., 'linux', 'win32', 'darwin'). The output should be user friendly names
"Linux", "Windows", "MacOS"
"""

# Created a platform variable to get the current platform and used conditional statements to check which platform it is.
# Then printed out the platform with their aligned window friendly names.
# Used startswith for linux incase of different distributions.
print()
print("TASK 6")
# Sys platforms defines based on what OS you are using right now.
platform = sys.platform
if platform.startswith('linux'):
    platform_name = "Linux"
elif platform == 'win32':
    platform_name = "Windows"
elif platform == 'darwin':
    platform_name = "MacOS"
else:
    platform_name = "Unknown"
print(f"Platform: {platform_name}")