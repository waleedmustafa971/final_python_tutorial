# user.py

# user.py (Module for the User class and OOP)


class User:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def __repr__(self):
        return f"User(name='{self.name}', age={self.age}, occupation='{self.occupation}')"

    def to_dict(self):
        return {"name": self.name, "age": self.age, "occupation": self.occupation}
