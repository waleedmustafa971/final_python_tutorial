# If you want to allow a function to accept an arbitrary number of arguments, use *args for positional arguments and **kwargs for keyword arguments.

def print_fruits(*fruits):
    for fruit in fruits:
        print(fruit)

print_fruits("apple", "banana", "cherry")

# Using **kwargs for arbitrary keyword arguments:

# def describe_person(**details):
#     for key, value in details.items():
#         print(f"{key}: {value}")

# describe_person(name="Waleed", age=30, job="Developer")


