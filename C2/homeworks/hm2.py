# Homework 2 - first_last & camel

def first_last(st: str, *args: str) -> list[tuple]:
    """Find the first and last position of provided letters in the provided string"""
    
    # Check for a valid type
    if not isinstance(st, str):
        raise TypeError(f"Invalid argument type. Expected {str}, got {type(st)}")
    
    # Check if any args provided
    if not args:
        return
    
    result = []
    
    # Convert string to casefold and create a reversed version
    st_casefold = st.casefold()
    st_reversed = st_casefold[::-1]
    
    # Getting the length of the string
    st_len = len(st)
    
    # Iterating over each given character
    for letter in args:
        
        # Check for a valid type
        if not isinstance(letter, str):
            raise TypeError(f"Invalid argument type. Expected {str}, got {type(st)}")

        # Casefold the letter
        letter = letter.casefold()
        
        # Check if the letter is present
        if letter not in st_casefold:
            result.append((None, None))
            continue
        
        # Else: append a tuple with 2 integers(first and last position) to result
        result.append((st_casefold.find(letter), st_len-st_reversed.find(letter)-1))
    
    # Return the result
    return result

def camel(st: str) -> str:
    """Convert the string to CaMeLcAsE"""
    
    # Check for a valid type
    if not isinstance(st, str):
        raise TypeError(f"Invalid argument type. Expected {str}, got {type(st)}")
    
    # Initialize the switch and result
    switch = True
    result = ''
    
    # Iterating over each character in the provided string
    for char in st:
        
        # Check if must change the letter to uppercase or lowercase
        if switch:
            char = char.upper()
        else:
            char = char.lower()
        
        # Appending the letter to the result
        result += char
        
        # If the character isn't a punctuation, flip the switch
        if char not in (' ', '.', ',', '!', '?', '-'):
            switch = not switch
    
    return result

st1 = "Задаючи завдання додому, вчителі мітять у учнів, а потрапляють у батьків."
st2 = "Ніколи! Ніколи не нюхайте як кипить чайник."
st3 = "Математичні завдання - це єдине місце, де хтось може купити 60 кавунів і ніхто його не запитає навіщо?"
st4 = "Як тільки зібрався взятися за розум, закінчився навчальний рік."
st5 = "Зник собака, дуже розумна. Кулька, якщо ти зараз це читаєш, подзвони додому!"

for i in (st1, st2, st3, st4, st5):
    print(camel(i))

st1 = 'Helpless'
print(first_last(st1, 'e'))