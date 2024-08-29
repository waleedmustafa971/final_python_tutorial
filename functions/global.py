# # Local Scope: Variables created inside a function are local to that function and cannot be accessed outside.

# # Global Scope: Variables defined outside all functions are global and can be accessed from any function.

# If you need to modify a global variable inside a function, use the global keyword.

x = 10  # Global variable

def modify_x():
    global x
    x = 5  # Modify the global variable

modify_x()
print(x)  # Output: 5


#######################
# Summary

# Functions allow you to encapsulate logic into reusable blocks of code.
# Arguments enable you to pass data to functions.
# Return statements allow you to return a result from the function.
# Default arguments provide a default value when none is passed.
# Keyword arguments offer flexibility in how arguments are passed.
# Arbitrary arguments let you handle variable numbers of arguments.
# Lambda functions allow concise function definitions.
# Scopes manage where variables are accessible in your code.
