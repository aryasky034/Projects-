import itertools
import ctypes

def set_color(color_code):
    # Set the color of the command prompt
    ctypes.windll.kernel32.SetConsoleTextAttribute(ctypes.windll.kernel32.GetStdHandle(-11), color_code)

def brute_force(password):
    max_len = len(password)
    characters = '0123456789'  # Numeric characters only

    # Generate all combinations of allowed characters
    for length in range(1, max_len + 1):
        for attempt in itertools.product(characters, repeat=length):
            attempt_str = ''.join(attempt)
            print(f'Attempting: {attempt_str}')
            if attempt_str == password:
                print(f"Password found: {attempt_str}")
                return

    print("Password not found.")

if __name__ == "__main__":
    # Set the console text color to green (color code 0A)
    set_color(0x0A)  # 0x0A is green text on black background

    password = input("Enter the password to crack (max length 4, numeric only): ")
    
    if len(password) > 4 or not password.isdigit():
        print("Error: Password must be numeric and not exceed a maximum length of 4.")
    else:
        print("Starting brute-force attack...")
        brute_force(password)

    # Optionally reset color to default (white on black)
    set_color(0x07)  # 0x07 is the default color (light gray on black)
