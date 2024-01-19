# Homework 1 - Password validator

def password_validator(password: str) -> dict[str, bool]:

    # Check if the password is a string
    if not isinstance(password, str):
        raise TypeError('Password must be a string')
    
    # Check if the password is an empty string
    if not password:
        raise ValueError('Password cannot be empty')
    
    # Convert the password to a set
    password_set = set(password)
    
    # Define the allowed characters
    allowed_chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789*-#')
    
    # Define must-have characters
    uppercase_chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    lowercase_chars = set('abcdefghijklmnopqrstuvwxyz')
    digit_chars = set('0123456789')
    special_chars = set('*-#')
    
    # Run checks and make a dictionary bool value for each condition
    check_dict = {
        'length': 8 <= len(password) <= 12,
        'uppercase': bool(password_set.intersection(uppercase_chars)),
        'lowercase': bool(password_set.intersection(lowercase_chars)),
        'digit': bool(password_set.intersection(digit_chars)),
        'symbol': bool(password_set.intersection(special_chars)),
        'supported': password_set.issubset(allowed_chars)
    }
    return check_dict

if __name__ == '__main__':
    while True:
        password = input('Enter your password: ')
        result = password_validator(password)
        
        if not all(result.values()):
            print(f'\tPassword invalid\n\t{result}')
            continue
        
        print('\tPassword valid')