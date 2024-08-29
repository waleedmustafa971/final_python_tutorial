# You can provide default values for function arguments. If the caller doesn’t provide a value, the function uses the default.

def greet(name="Waleed"):
    print(f"Hello, {name}!")

greet()        # Output: Hello, Waleed!
greet("John")  # Output: Hello, John!
