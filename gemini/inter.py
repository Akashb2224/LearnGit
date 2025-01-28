def validate_username(user):
    if len(user) < 8:
        print("Username should be at least 8 characters long.")
        return False
    if not any(char.isupper() for char in user):
        print("Username should contain at least one uppercase letter.")
        return False
    return True

def validate_password(password):
    special_characters = "!@#$%^&*"
    if len(password) < 8:
        print("Password should be at least 8 characters long.")
        return False
    if not any(char.isupper() for char in password):
        print("Password should contain at least one uppercase letter.")
        return False
    if not any(char in special_characters for char in password):
        print("Password should contain at least one special character.")
        return False
    return True

# Get input from the user
username = input("Enter username: ")
password = input("Enter password: ")

# Validate the inputs
if validate_username(username) and validate_password(password):
    print("Username and password are valid!")
else:
    print("Invalid username or password.")
