import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    # Define character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Create a pool of characters based on user preferences
    character_pool = ""
    if use_uppercase:
        character_pool += uppercase_letters
    if use_lowercase:
        character_pool += lowercase_letters
    if use_digits:
        character_pool += digits
    if use_special:
        character_pool += special_characters

    # Ensure at least one character from each selected set is included
    password = []
    if use_uppercase:
        password.append(random.choice(uppercase_letters))
    if use_lowercase:
        password.append(random.choice(lowercase_letters))
    if use_digits:
        password.append(random.choice(digits))
    if use_special:
        password.append(random.choice(special_characters))

    # Fill the rest of the password length with random characters
    for _ in range(length - len(password)):
        password.append(random.choice(character_pool))

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    return ''.join(password)

# Example usage
if __name__ == "__main__":
    password = generate_password(length=16, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True)
    print(f"Generated Password is: {password}")
