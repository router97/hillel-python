def password_validator(password: str) -> bool:
    
    if 8 > len(password) or 12 < len(password):
        print('password length must be between 8 and 12 chars')
        return False
    
    print('password valid')
    return True

# У паролі повинні бути великі літери, малі символи, 
# числа та спеціальні знаки (з переліку *-# інші спецсимволи неприпустимі)

if __name__ == '__main__':
    while True:
        print(password_validator(input('Enter your password: ')))