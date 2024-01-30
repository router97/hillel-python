# Homework 4 - Human Faker

class Human:
    
    def __init__(self, 
                 adress: str, 
                 phone: str, 
                 job: str, 
                 salary: int):
        self.adress = adress
        self.phone = phone
        self.job = job
        self.salary = salary
    
    def show_info(self):
        info = '\n'.join([f"{key}: {value}" for key, value in self.__dict__.items()])
        print(info)

class Man(Human):
    
    def __init__(self, 
                 first_name: str, 
                 last_name: str, 
                 *args, 
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.first_name = first_name
        self.last_name = last_name

class Woman(Human):
    
    def __init__(self, 
                 first_name: str, 
                 last_name: str, 
                 *args, 
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.first_name = first_name
        self.last_name = last_name


if __name__ == '__main__':
    
    from faker import Faker
    faker = Faker('uk_UA')
    
    human = Human(faker.address(), faker.phone_number(), faker.job(), faker.random.randint(1000, 9999))
    man = Man(faker.first_name(), faker.last_name(), faker.address(), faker.phone_number(), faker.job(), faker.random.randint(1000, 9999))
    woman = Woman(faker.first_name(), faker.last_name(), faker.address(), faker.phone_number(), faker.job(), faker.random.randint(1000, 9999))
    
    human.show_info()
    print('-----')
    man.show_info()
    print('-----')
    woman.show_info()