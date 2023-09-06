##############This is a Password Strength Checker Project

#input
password= input("Enter password to your account")

import re

def is_strong_password(password):
    # Check if the password meets the following criteria:

    # At least 8 characters long
    if len(password) < 8:
        return False
    
    # Contains at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False

    # Contains at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False

    # Contains at least one digit
    if not re.search(r'[0-9]', password):
        return False

    # Contains at least one special character
    if not re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\-]', password):
        return False

    return True

if is_strong_password(password):
    print("Password is strong!")
else:
    print("Password is weak. Please choose a stronger password.")
