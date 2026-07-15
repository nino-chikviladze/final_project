import re

user_data = {
    "email": "user@mail.com",
    "name": "",
    "nickname": "george777",
    "password": "password123",
}

def register_user():
    print("<--- Registration Simulator --->")
    name = input("Enter your name (lowercase English letters only): ").strip()

    if not name:
        print("Error: String is empty")
        return

    if any(char.isdigit() for char in name):
        print("Error: Numeric value detected")
        return

    if any(char.isupper() for char in name):
        print("Error: Uppercase letters detected")
        return

    if re.search(r"[^\x00-\x7F]", name):
        print("Error: Non-Latin characters detected")
        return

    if not name.replace(" ", "").isalpha():
        print("Error: Special symbols detected")
        return

    user_data["name"] = name
    print("\nRegistration Successful! Profile data:")
    print(f"Email: {user_data['email']}")
    print(f"Name: {user_data['name']}")
    print(f"Nickname: {user_data['nickname']}")
    print(f"Password: {user_data['password']}")

register_user()