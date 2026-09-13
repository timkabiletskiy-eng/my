from gettext import find


class Human:
    def __init__(self ,name):
        self.name = name

class Car:
    def __init__(self, model):
        self. model = model
        self.passengers = []

    def add_passenger(self, human):
        self.passengers.append(human)

    def info(self):
        print(f"Auto : {self.model}")
        if self.passengers:
            print("Зараз їдуть:")
            for p in self.passengers:
                print(p.name)
        else:
            print("пасажири відсутні")

    def remove_pssenger(self, name):
        for h in self.passengers:
            if h.name == name:
                self.passengers.remove(h)

h1 = Human("Serg")
h2 = Human("Anna")
h3 = Human("Oleg")

car = Car("Tesla Model 13")

car.add_passenger(h1)
car.add_passenger(h2)
car.add_passenger(h3)
car.info()

car.remove_pssenger("Oleg")
car.info()