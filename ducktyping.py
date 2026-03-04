class Animal:
    Alive = True

class Dog(Animal):
    def speak(self):
        print("BOW BOW")

class Cat(Animal):
    def speak(self):
        print("Meow")

class Car(Animal):
    def speak(self):
        print("HONK")

animal = [Dog(), Cat(), Car()]
for anima in animal:
    anima.speak()
    print(anima.Alive)
Car.speak()