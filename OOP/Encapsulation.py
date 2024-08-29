# Encapsulation is the bundling of data (attributes) and methods that operate on the data into a single unit or class. It restricts direct access to some of the object’s components, which helps in data protection.

# You can control the visibility of attributes and methods using:

# Public (default): Accessible from outside the class.
# Private: Use double underscore __ to make an attribute or method private, preventing it from being accessed directly from outside the class.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner         # Public attribute
        self.__balance = balance   # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance

account = BankAccount("Waleed", 1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500

# In this example, the balance is private, so it can't be accessed directly from outside the class. It can only be accessed or modified through the class's methods.

