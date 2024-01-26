# Homework 4 - Human Faker

from faker import Faker

faker = Faker()


class Human:
    
    def __init__(self, 
                 adress: str, 
                 phone: str, 
                 job: str,
                 salary: float):
        self.adress = adress
        self.phone = phone
        self.job = job
        self.salary = salary
    
    def show_info(self):
        result = ''
        for i in [f"{key}: {value}\n" for key, value in self.__dict__.items()]:
            result += i
        print(result)

class Man(Human):
    pass

class Woman(Human):
    pass

if __name__ == '__main__':
    person1 = Human(faker.address(), faker.phone_number(), faker.job(), faker.random.randint(1000, 9999))
    person1.show_info()