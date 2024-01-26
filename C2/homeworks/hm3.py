# Homework 2 - collect_the_bag

import hm3_data as data

def collect_the_bag() -> None:
    
    # Ask for the week day
    while True:
        
        # Get user input
        selected_day = input('Введіть день тижня: ').casefold()
        
        # Validate given day
        if selected_day in data.schedule:
            break
        print('Олух ти, Санек! Давай ще раз)')
    
    # Get a list of books which are to be collected
    books_left = list(data.schedule[selected_day])
    books_collected = []
    
    # Ask for book names
    while True:
        
        # Check if there are any books left to collect
        if not books_left:
            break
        
        # Get user input
        book = input('Введіть назву книжки: ').title()
        
        # Check if the book isn't valid
        if not book in books_left:
            print("Олух ти, Санек! Давай ще раз)")
            continue
        
        # Otherwise, remove the book from the to-collect list
        books_left.remove(book)
        books_collected.append(book)
        print("Добре Саня, вгадав. Все ж таки задатки розуму присутні")
    
    # End the function
    print(f"Зібрано книжки: {books_collected}\nФункція закінчила свою працю")

if __name__ == '__main__':
    collect_the_bag()