from faker import Faker
from fake_passager_entity import FakePassager
import random
import time


class FakeDataMake:
    def __init__(self):
        pass

    def get_passager(self):
        try:
            fake = Faker("zh_CN")
            fake_passager = FakePassager()
            fake_passager.paperstype = fake.bothify(text='?', letters="DP")
            fake_passager.papersnumber = fake.bothify(text='?########', letters="EMD")
            fake_passager.nationality = str(random.randint(1, 143))
            fake_passager.name = fake.last_romanized_name() + ' ' + fake.last_romanized_name()
            fake_passager.gender = fake.bothify(text='?', letters="FM")
            fake_passager.birthdate = fake.date()
            fake_passager.birthplace = fake.address()
            fake_passager.date = fake.date()
            return fake_passager
        except Exception:
            print("ERR")


    def make_fake_data(self):
        fake = Faker("zh_CN")
        # Faker.seed(1)

        fake_passager = FakePassager()
        i = 1
        # x = 1
        last_time = time.time()
        while i <= 2:
            fake_passager.paperstype = fake.bothify(text='?', letters="DP")
            fake_passager.papersnumber = fake.bothify(text='?########', letters="EMD")
            fake_passager.nationality = str(random.randint(1, 143))
            fake_passager.name = fake.last_romanized_name() + ' ' + fake.last_romanized_name()
            fake_passager.gender = fake.bothify(text='?', letters="FM")
            fake_passager.birthdate = fake.date()
            fake_passager.birthplace = fake.address()
            fake_passager.date = fake.date()

            print('------------------------------------')
            print("Order: " + str(i))
            print('Passport Type: ' + fake_passager.paperstype)
            print('Passport Number: ' + fake_passager.papersnumber)
            print('Nationality: ' + fake_passager.nationality)
            print('Name: ' + fake_passager.name)
            print('Gender: ' + fake_passager.gender)
            print('Birth Date: ' + fake_passager.date)
            print('Birth Place: ' + fake_passager.birthplace)
            print('Fake Passager: ' + str(fake_passager.__dict__))
            print('------------------------------------')
            i = i + 1

        current_time = time.time()
        print("Time Consuming： {}".format(current_time - last_time))
        return fake_passager

fdm = FakeDataMake()
fdm.make_fake_data()
