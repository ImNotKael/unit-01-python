import os
import os.path
import sys
"""
Task 1 (os module):
Write a Python program that prints the current folder (working directory) using the os module.
"""
print("Task 1:")
directory = os.getcwd#create a variable for directory

print("Current working directory:", directory)#print the working directory

"""
Task 2 (os module):
Create a new directory called "test_folder" in the current directory.
Then print a list of all files and directories in the current directory.
"""
print("Task 2:")
test_folder = "test_folder"#create a variable for the new folder

if not os.path.exists(test_folder):#checks if the folder exists
    os.mkdir(test_folder)
    print(f"Directory '{test_folder}' created.")
else:
    print(f"Directory '{test_folder}' already exists.")

list = os.listdir('.')#list all the files and directs in the test folder

print("Files and directories in the current directory:")
for item in list:#prints each item in the list
    print(item)

"""
Task 3 (os module):
Write a program that checks if a directory called "data" exists in the current 
working directory. If it doesn't exist, create it. If it does exist, print 
"Directory already exists."
"""
print("Task 3:")
directory_name = "data"#creates a vairbale for the directory name
directory_path = os.getcwd()#create a variable for the directory path
direct_path = os.path.join(directory_path, directory_name)#creates a vraible for direct path
if not os.path.exists(direct_path):#checks if the directory exists
    print("Directory already exists.")

else:
    os.mkdir(direct_path)
    print(f"Directory '{directory_name}' created at {direct_path}.")

"""
Task 4 (os.path module):
Write a program that checks if a file called "config.txt" exists in the current directory.
If it exists, print its path. If it doesn't exist, print "File not found."
"""
print("Task 4:")
filename = "config.txt"#creates a varibale for the filename

file_path = os.path.join(os.getcwd(), filename)#create file path by joining the current working directory and filename

if not os.path.isfile(file_path):#checks if the file is found
    print(f"File found at: {file_path}")
else:
    print("File not found.")

"""
Task 5 (sys module):
Write a program that prints the Python version you are currently using.
"""
print("Task 5:")
print("Python version:", sys.version)#prints the python version

"""
Task 6 (sys module):
Write a program that prints the platform your Python interpreter is running on
(e.g., 'linux', 'win32', 'darwin'). The output should be user friendly names
"Linux", "Windows", "MacOS"
"""
print("Task 6:")
platform_ID = sys.platform#creates a vairable for the platform IF
platform = {#creats a dictionary for the platform names
    'linux': 'linux',
    'win32': 'Windows',
    'darwin': 'MacOS',
    'e.g.,': 'e.g.,'
}
print("Platform:", platform.get(platform_ID, f"Unknown ({platform_ID})"))#prints the platform name or unknown
