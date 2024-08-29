# A module is a file containing Python definitions and statements. Modules allow you to organize your code into smaller, manageable pieces and promote code reuse.

# Creating and Using a Module
# You can create your own module by writing Python code in a .py file and then importing that file into another script.

# 1-Create a module file (let’s call it mymodule.py):
# mymodule.py
def greet(name):
    print(f"Hello, {name}!")

PI = 3.14159

# 2-Use the module in another script:
# main.py
import mymodule

mymodule.greet("Waleed")  # Output: Hello, Waleed!
print(mymodule.PI)        # Output: 3.14159


# Different Import Methods:
# import module_name: Imports the entire module.
# from module_name import function_name: Imports specific functions or variables from the module.
# from module_name import *: Imports everything from the module (not recommended for large projects).

# Example:

from mymodule import greet, PI

greet("Waleed")  # Output: Hello, Waleed!
print(PI)        # Output: 3.14159


###################


# 2. Packages in Python

# A package is a collection of modules organized in directories that give structure to your Python project. A package is simply a directory with a special __init__.py file (this file can be empty or contain initialization code for the package).

# my_package/
#     __init__.py
#     module1.py
#     module2.py

# To use a package, you import it just like you would a module.

from my_package import module1

module1.some_function()


# 3. File Handling in Python

# Python allows you to read from and write to files. This is crucial for applications that need to persist data, such as saving user input, reading configurations, or logging information.

# Opening a File
# The built-in open() function is used to open a file. It returns a file object that you can use to read, write, or append data.

# Modes:
# 'r': Read (default)
# 'w': Write (overwrites the file)
# 'a': Append (adds content to the end of the file)
# 'b': Binary mode
# '+': Read and write

file = open("example.txt", "w")  # Open file in write mode
file.write("Hello, Waleed!\n")   # Write to the file
file.close()                     # Close the file

# Reading a File

# You can read the entire file content using the read() method or line by line using the readline() or readlines() methods.

file = open("example.txt", "r")  # Open file in read mode
content = file.read()            # Read the entire content
print(content)                   # Output: Hello, Waleed!
file.close()                     # Close the file

# 4. Context Managers

# It’s a good practice to use context managers (with statement) when working with files. This ensures that files are properly closed even if an error occurs during file operations.
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # Output: Hello, Waleed!

    # The with statement automatically closes the file when the block of code inside it is finished.

# 5. Reading and Writing CSV Files

# CSV (Comma-Separated Values) is a common file format used to store tabular data. Python’s csv module allows you to read from and write to CSV files.

# Example:

# Writing to a CSV file:

import csv

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Occupation"])
    writer.writerow(["Waleed", 30, "Developer"])

    # Reading from a CSV file:
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# 6. Working with JSON Files

# JSON (JavaScript Object Notation) is a popular format for storing and exchanging data. Python’s json module provides methods for working with JSON.

# Dumping data to a JSON file:

import json

data = {"name": "Waleed", "age": 30, "occupation": "Developer"}

with open("data.json", "w") as file:
    json.dump(data, file)

# Loading data from a JSON file:

with open("data.json", "r") as file:
    data = json.load(file)
    print(data)  # Output: {'name': 'Waleed', 'age': 30, 'occupation': 'Developer'}

# 7. Exception Handling in File Operations

# When working with files, errors can occur (e.g., file not found, permission issues). Python provides exception handling to manage these errors gracefully using try-except blocks.

try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")


####################################
# Summary of Key Concepts
# Modules: Organize your code into separate files to promote reusability.
# Packages: Organize related modules into directories, adding structure to larger projects.
# File Handling: Read from and write to files using built-in functions and context managers.
# CSV/JSON Handling: Use built-in modules like csv and json to work with data stored in these formats.
# Exception Handling: Manage potential errors that occur during file operations using try-except.
















