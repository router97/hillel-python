# Homework 24 - Vladyslav


def repeated(input_str: str) -> bool:
    """Check if a given string consists of sub-string patterns"""
    # Variables
    checking = ''
    string_length = len(input_str)
    
    # Check if the given string is more than 1 character
    if len(input_str) <= 1:
        return False
    
    # Setting the amount of characters to check, because a pattern cannot be more than half of the string's length
    check_amount = string_length // 2 + string_length % 2   
    
    # Going through each element in the string
    for character in input_str[:check_amount]:
        
        # Enlarging the checking area
        checking += character
        
        # Making a list of anything that's not the possible pattern
        non_pattern_elements = [el for el in input_str.split(checking) if el != checking and el != '']
        
        # If the list is empty, we found the pattern
        if not non_pattern_elements:
            return True
    
    # If not, no pattern found
    return False


if __name__ == '__main__':
    while True:
        user_input = input('Enter your string (type "exit" to quit): ')
        if user_input.lower() == 'exit':
            break
        print(repeated(user_input))