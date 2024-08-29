# file_handler.py


# file_handler.py (Module for File Handling, including CSV and JSON handling)


import csv
import json

class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def write_text(self, data):
        try:
            with open(self.filename, 'w') as file:
                file.write(data)
            print("Data written to text file successfully.")
        except Exception as e:
            print(f"Error writing to file: {e}")

    def read_text(self):
        try:
            with open(self.filename, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print("File not found!")
        except Exception as e:
            print(f"Error reading file: {e}")
            return None

    def write_csv(self, data):
        try:
            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Age", "Occupation"])
                for user in data:
                    writer.writerow([user.name, user.age, user.occupation])
            print("Data written to CSV file successfully.")
        except Exception as e:
            print(f"Error writing to CSV file: {e}")

    def read_csv(self):
        try:
            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                return [row for row in reader]
        except FileNotFoundError:
            print("CSV file not found!")
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return None

    def write_json(self, data):
        try:
            with open(self.filename, 'w') as file:
                json.dump([user.to_dict() for user in data], file)
            print("Data written to JSON file successfully.")
        except Exception as e:
            print(f"Error writing to JSON file: {e}")

    def read_json(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("JSON file not found!")
        except Exception as e:
            print(f"Error reading JSON file: {e}")
            return None
