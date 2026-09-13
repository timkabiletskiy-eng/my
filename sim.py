import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 30
        self.progress = 10
        self.energy = 50
        self.alive = True
        self.money = 500

    def study(self):
        print("я пішов до академії IT STEP")
        self.energy -= 3
        self.progress += 1.5
        self.gladness -= 1
        self.money -= 50

    def chill(self):
        print("Я пішов з друзяками гуляти")
        self.gladness += 2
        self.energy -= 3
        self.progress -= 1
        self.money -= 100

    def sleep(self):
        print("Я пішов спати")
        self.energy += 5
        self.gladness += 1

    def eat(self):
        print("Я смачно поїв")
        self.energy += 3
        self.gladness += 1
        self.progress -= 0.2
        self.money -= 80

    def job(self):
        print("Я пахаю на роботі")
        self.energy -= 3
        self.gladness -= 3
        self.progress -= 0.2
        self.money += 250

    def is_alive(self):
        if self.progress <= 0:
            print("Я тупий")
            self.alive = False
        if self.gladness <= 0:
            print("В мене дипресія")
            self.alive = False
        if self.progress > 100:
            print("Я став академіком")
        if self.energy <= 0:
            print("Я знесилений")
            self.alive = False
        if -50 < self.money <= 0:
            print("Я бомж, треба на роботу")
            self.job()
        if self.money < -50:
            print("Я бомж")
            self.alive = False

    def live(self, day):
        print(f"День №{day} з життя {self.name}")
        print("-"*30)
        random.choice([self.study, self.chill, self.sleep, self.eat, self.job])()
        #       match rnd:
 #           case (1):
  #              self.study()
  #          case(2):
  #              self.chill()
  #          case(3):
  #              self.sleep()
   #         case(4):
   #             self.eat()

        self.info()
        self.is_alive()
        print()


    def info(self):
        print(f"На сьгодн {self.name} має")
        print(f"Задоволення: {self.gladness}")
        print(f"Знання: {self.progress}")
        print(f"Енергія: {self.energy}")
        print(f"Грощі: {self.money}")


student = Student("Vasya")
day = 1
while student.alive == True:
    day += 1
    student.live(day)