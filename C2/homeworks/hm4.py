# Homework 4 - Human Faker

class Human:
    
    def __init__(self, 
                 address: str, 
                 phone: str, 
                 job: str, 
                 salary: int):
        self.adress = address
        self.phone = phone
        self.job = job
        self.salary = salary
    
    def show_info(self):
        info = '\n'.join([f"{key}: {value}" for key, value in self.__dict__.items()])
        print(info)

class Man(Human):
    
    def __init__(self, 
                 address: str, 
                 phone: str, 
                 job: str, 
                 salary: int, 
                 first_name: str, 
                 last_name: str):
        super().__init__(address, phone, job, salary)
        self.first_name = first_name
        self.last_name = last_name

class Woman(Human):
    
    def __init__(self, 
                 address: str, 
                 phone: str, 
                 job: str, 
                 salary: int, 
                 first_name: str, 
                 last_name: str):
        super().__init__(address, phone, job, salary)
        self.first_name = first_name
        self.last_name = last_name


if __name__ == '__main__':
    
    from faker import Faker
    faker = Faker('uk_UA')
    
    human = Human(faker.address(), faker.phone_number(), faker.job(), faker.random.randint(1000, 9999))
    man = Man(faker.address(), faker.phone_number(), faker.job(), faker.random.randint(1000, 9999), faker.first_name(), faker.last_name())
    woman = Woman(faker.address(), faker.phone_number(), faker.job(), faker.random.randint(1000, 9999), faker.first_name(), faker.last_name())
    
    human.show_info()
    print('-----')
    man.show_info()
    print('-----')
    woman.show_info()