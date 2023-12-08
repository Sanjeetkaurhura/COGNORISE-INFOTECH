import random
import string

def generate_password(length=12):
    # Define characters to include in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password using the specified length
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Example: Generate a password of length 16
password = generate_password(16)
print("Generated Password:", password)
