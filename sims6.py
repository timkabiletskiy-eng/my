import random
class Human:
    def __init__(self, name, car=None, job=None):
        self.name = name
        self.house = House()
        self.car = car
        self.job = job
        self.money = 100

    def work(self):
        pass

    def shopping(self):
        self.money -= random.randint(1, 10)
        self.house.food -= random.randint(1, 10)
        if self.car != None:
            print("go to the shop on my legs")
        else:
            if self.car.drive(random.randint(1, 10)):
                print("go to the shop on my car")
            else:
                print("go to the shop on my legs")

    def eat(self):
        pass

    def chill(self):
        pass

    def cleaning(self):
        pass

    def info(self):
        pass

    def live(self, day):
        pass

    def is_alive(self):
        return self.money > 0

class Car:
    def __init__(self, model):
        self.model = model
        self.fuel = 60
        self.state = 100

    def drive(self, length):
        rashid = length*0.1
        if self.fuel - rashid > 0:
            print(f"Ми проїхали {length} км, витратили {rashid} л палного")
            self.fuel -= rashid
            self.state -= length * 0.01
            return True
        else:
            print("Подорож не можлива. немає пального")
            return False

    def add_fuel(self):
        pass

    def __str__(self):
        pass

class job:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        pass

class House:
    def __init__(self):
        self.food = 0
        self.pollution = 0

    def __str__(self):
        pass