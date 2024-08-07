import random
import string

def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4")
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    all_characters = lowercase + uppercase + digits + special_characters
    password += random.choices(all_characters, k=length-4)

    random.shuffle(password)

    return ''.join(password)

try:
    password_length = int(input("Enter the desired length for the password (at least 4): "))
    generated_password = generate_password(password_length)
    print("Generated password:", generated_password)
except ValueError as e:
    print(e)
