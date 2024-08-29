# main.py

from user_management.user import User
from user_management.file_handler import FileHandler

def main():
    # Creating some users
    user1 = User("Waleed", 30, "Developer")
    user2 = User("Alice", 25, "Data Scientist")
    user3 = User("Bob", 28, "Designer")
    
    users = [user1, user2, user3]

    # Handling text files
    text_handler = FileHandler("users.txt")
    text_handler.write_text("\n".join([str(user) for user in users]))
    print("Text file content:")
    print(text_handler.read_text())

    # Handling CSV files
    csv_handler = FileHandler("users.csv")
    csv_handler.write_csv(users)
    print("\nCSV file content:")
    print(csv_handler.read_csv())

    # Handling JSON files
    json_handler = FileHandler("users.json")
    json_handler.write_json(users)
    print("\nJSON file content:")
    print(json_handler.read_json())

if __name__ == "__main__":
    main()
