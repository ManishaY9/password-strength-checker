import re

def check_password_strength(password):
    """
    Check the strength of a password and provide detailed feedback.
    
    Args:
        password (str): The password to be checked.
    
    Returns:
        dict: A dictionary containing:
            - is_strong (bool): Whether the password meets all criteria
            - feedback (list): Suggestions for improvement
    """
    # Initialize result dictionary
    result = {
        'is_strong': True,
        'feedback': []
    }
    
    # Check 1: Minimum length of 8 characters
    if len(password) < 8:
        result['is_strong'] = False
        result['feedback'].append("- Password should be at least 8 characters long")
    
    # Check 2: Contains at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        result['is_strong'] = False
        result['feedback'].append("- Add at least one uppercase letter")
    
    # Check 3: Contains at least one lowercase letter
    if not re.search(r'[a-z]', password):
        result['is_strong'] = False
        result['feedback'].append("- Add at least one lowercase letter")
    
    # Check 4: Contains at least one digit
    if not re.search(r'\d', password):
        result['is_strong'] = False
        result['feedback'].append("- Include at least one number")
    
    # Check 5: Contains at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        result['is_strong'] = False
        result['feedback'].append("- Add at least one special character")
    
    return result

def main():
    """
    Main function to interactively check password strength.
    """
    print("Password Strength Checker")
    print("------------------------")
    
    while True:
        # Get password input
        password = input("\nEnter a password to check (or 'quit' to exit): ")
        
        # Allow user to exit
        if password.lower() == 'quit':
            print("Exiting password strength checker.")
            break
        
        # Check password strength
        strength_result = check_password_strength(password)
        
        # Provide feedback
        if strength_result['is_strong']:
            print(" Strong Password: Your password meets all security criteria!")
        else:
            print(" Weak Password. Please improve:")
            for suggestion in strength_result['feedback']:
                print(suggestion)

if __name__ == "__main__":
    main()