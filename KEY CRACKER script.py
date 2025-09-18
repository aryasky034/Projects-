import itertools
import ctypes
import string
import getpass  # Importing getpass for secure password input

def set_color(color_code):
    # Set the color of the command prompt
    ctypes.windll.kernel32.SetConsoleTextAttribute(ctypes.windll.kernel32.GetStdHandle(-11), color_code)

def brute_force(password):
    max_len = len(password)
    # Include special characters and spaces
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + string.whitespace

    # Initialize an empty list to hold the current password attempt
    current_attempt = ['_'] * max_len

    for index in range(max_len):
        for char in characters:
            current_attempt[index] = char  # Set the current character
            attempt_str = ''.join(current_attempt)
            print(f'Attempting: {attempt_str}')
            if attempt_str == password:
                print(f"Password found: {attempt_str}")
                return
            # If the current character matches the password character, move to the next character
            if password[index] == char:
                print(f"Character '{char}' matched at position {index}.")
                break  # Move to the next character

    print("Password not found.")

if __name__ == "__main__":
    # Set the console text color to green (color code 0A)
    set_color(0x0A)  # 0x0A is green text on black background

    # Use getpass to securely input the password without displaying it
    password = getpass.getpass("Enter the password to crack (length between 4 and 20, alphanumeric and special characters): ")
    
    if len(password) < 4 or len(password) > 20 or not all(c.isprintable() for c in password):
        print("Error: Password must be printable characters and between 4 and 20 characters long.")
    else:
        print("Starting brute-force attack...")
        brute_force(password)

    # Optionally reset color to default (white on black)
    set_color(0x07)  # 0x07 is the default color (light gray on black)
