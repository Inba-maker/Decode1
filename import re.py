import re

def check_password_strength(password):
    score = 0

    # Length check
    if len(password) >= 8:
        score += 1

    # Uppercase letter check
    if re.search(r"[A-Z]", password):
        score += 1

    # Number check
    if re.search(r"\d", password):
        score += 1

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Strength result
    if score <= 1:
        return "Weak Password"
    elif score <= 3:
        return "Medium Password"
    else:
        return "Strong Password"

password = input("Enter your password: ")
result = check_password_strength(password)

print("\nPassword Strength:", result)