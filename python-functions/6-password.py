def validate_password(password):
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return False

    # Check if the password contains at least one uppercase letter, one lowercase letter, and one digit
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True

    if not (has_uppercase and has_lowercase and has_digit):
        return False

    # Check if the password contains spaces
    if ' ' in password:
        return False

    # If all checks pass, the password is valid
    return True


# Write a Python function called validate_password 
# that takes a password as input and performs the following checks:

# The password should be at least 8 characters long.
# The password should contain at least one uppercase letter, one lowercase letter, and one digit.
# The password should not contain spaces.

# Prototype: def validate_password(password)

# Returns True if the password passes all the checks, and False otherwise.

# You are not allowed to import any module.