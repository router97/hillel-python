# Homework 4 - Intern class


class Intern:
    
    def __init__(self, first_name: str, last_name: str, address: str, phone: str, email: str):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone = phone
        self.email = email
    
    def __del__(self):
        print(f'Deleting intern {self.first_name} {self.last_name}')
    
    def getdata(self) -> None:
        self.first_name = input('Enter first name: ')
        self.last_name = input('Enter last name: ')
        self.address = input('Enter address: ')
        self.phone = input('Enter phone number: ')
        self.email = input('Enter email: ')
    
    def putdata(self) -> None:
        print(self.__dict__)

class NewIntern(Intern):
    
    def show_info(self) -> None:
        print(self.__dict__)


if __name__ == '__main__':
    
    from faker import Faker
    faker = Faker('uk_UA')
    
    intern = Intern(faker.first_name(), faker.last_name(), faker.address(), faker.phone_number(), faker.email())
    intern.putdata()
    del intern
    
    new_intern = NewIntern(faker.first_name(), faker.last_name(), faker.address(), faker.phone_number(), faker.email())
    new_intern.show_info()
    del new_intern