def password_validator(password: str) -> dict:
    
    if not isinstance(password, str):
        raise ValueError('Password must be a string')
    
    check_dict = {
        'length': True,
        'uppercase': False,
        'lowercase': False,
        'digit': False,
        'symbol': False,
        'supported': True
    }
    
    if 8 > len(password) or 12 < len(password):
        check_dict['length'] = False
    
    for char in password:
        if char.isupper():
            check_dict['uppercase'] = True
        elif char.islower():
            check_dict['lowercase'] = True
        elif char.isdigit():
            check_dict['digit'] = True
        elif char in '*-#':
            check_dict['symbol'] = True
        else:
            check_dict['supported'] = False
    
    return check_dict

print(password_validator('okaylilbro'))

# if __name__ == '__main__':
#     while True:
#         print(password_validator(input('Enter your password: ')))