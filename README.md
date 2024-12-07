# Password Strength Checker

## Overview

A Python script that provides comprehensive password strength validation, helping users create more secure passwords by evaluating them against multiple security criteria.

## Features

- Single, efficient function for password strength checking
- Detailed feedback on password weaknesses
- Interactive command-line interface
- Easy to use and extend

## Prerequisites

- Python 3.6+
- No external libraries required (uses built-in `re` module)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/password-strength-checker.git
cd password-strength-checker
```

2. Verify Python installation:
```bash
python --version
```

## Usage

### Running the Script

```bash
python password_strength_checker.py
```

### Password Strength Criteria

A strong password must meet ALL of these requirements:
- Minimum length of 8 characters
- Contains at least one uppercase letter
- Contains at least one lowercase letter
- Contains at least one digit
- Contains at least one special character

### Example Interactions

```
Password Strength Checker
------------------------

Enter a password to check (or 'quit' to exit): weakpass
 Weak Password. Please improve:
- Add at least one uppercase letter
- Include at least one number
- Add at least one special character

Enter a password to check (or 'quit' to exit): StrongP@ss123
Strong Password: Your password meets all security criteria!

Enter a password to check (or 'quit' to exit): quit
Exiting password strength checker.
```

## Customization

You can easily modify the script to:
- Add more complexity checks
- Change special character set
- Implement additional password validation rules

## Security Notes

- This is a basic password strength checker
- Always use additional security measures
- Never store passwords in plain text
