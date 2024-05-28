import random
import string

def generate_password(length=12):
    """
    Generate a random password.

    Parameters:
    length (int): The length of the generated password. Default is 12.

    Returns:
    str: A randomly generated password.
    """
    # Define the possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    # Example usage
    password_length = 16  # Specify the length of the password
    generated_password = generate_password(password_length)
    print(f"Generated password: {generated_password}")
