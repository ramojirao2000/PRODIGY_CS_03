import re

def check_password_strength(password):
    # Initialize criteria
    length_error = len(password) < 8
    lowercase_error = re.search(r"[a-z]", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Count how many conditions are met
    score = 5 - sum([length_error, lowercase_error, uppercase_error, digit_error, special_char_error])

    # Assess strength
    if score == 5:
        strength = "Very Strong 💪"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak 😟"

    # Prepare feedback
    feedback = []
    if length_error:
        feedback.append("⚠️ Use at least 8 characters.")
    if lowercase_error:
        feedback.append("⚠️ Include at least one lowercase letter.")
    if uppercase_error:
        feedback.append("⚠️ Include at least one uppercase letter.")
    if digit_error:
        feedback.append("⚠️ Include at least one digit.")
    if special_char_error:
        feedback.append("⚠️ Include at least one special character (!@#$...).")

    return strength, feedback


# Example usage
if __name__ == "__main__":
    password = input("Enter your password: ")
    strength, feedback = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Suggestions to improve your password:")
        for f in feedback:
            print(f" - {f}")
