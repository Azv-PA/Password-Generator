import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    # add characters based on the parameters
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_requirement = False
    has_number = False
    has_special = False

    # Generate password if it meets the requirements
    while not meets_requirement or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits: 
            has_number = True
        elif new_char in special:
            has_special = True

        # Check if all requirements are met
        meets_requirement = True
        if numbers:
            meets_requirement = has_number
        if special_characters:
            meets_requirement = meets_requirement and has_special
        if len(pwd) >= min_length:
            break

    return pwd

print(generate_password(16))
