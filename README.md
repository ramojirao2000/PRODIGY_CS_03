# Password Complexity Checker

This Python script evaluates the strength of a password based on the following criteria:

- Minimum length of 8 characters
- At least one lowercase letter
- At least one uppercase letter
- At least one digit
- At least one special character (e.g., !, @, #, etc.)

## How It Works

The script checks the entered password against the five criteria above and categorizes the password strength as:

- **Strong** – meets all five criteria
- **Moderate** – meets 3 or 4 criteria
- **Weak** – meets fewer than 3 criteria

It also provides feedback on any missing requirements.

## How to Run

1. Ensure you have Python installed (version 3.x).

2. Save the script into a file, for example, `passwordComplexityChecker.py`.

3. Open a terminal or command prompt in the script's directory.

4. Run the script using the following command:

```bash
python passwordComplexityChecker.py
