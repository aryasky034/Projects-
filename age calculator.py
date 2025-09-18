from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# Input: Enter your birthdate in the format YYYY-MM-DD
birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_input, "%Y-%m-%d")

age = calculate_age(birthdate)
print(f"You are {age} years old.")
