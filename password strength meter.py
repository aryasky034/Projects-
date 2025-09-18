import re

def password_strength(password):
    # Initialize strength score
    score = 0

    # Check length
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1

    # Check for digits
    if re.search(r'[0-9]', password):
        score += 1

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1

    # Determine strength
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Moderate"
    else:
        return "Strong"

# Example usage
password = input("Enter your password: ")
strength = password_strength(password)
print(f"Password strength: {strength}")
