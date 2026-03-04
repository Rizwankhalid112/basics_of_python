class RadioMixin:
    def play_music(self, station):
        print(f"🎶 Now playing {station} on the radio!")

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle, RadioMixin): 
    def drive(self):
        print(f"The {self.brand} car is driving on the road.")

class Boat(Vehicle, RadioMixin): 
    def sail(self):
        print(f"The {self.brand} boat is sailing on the water.")

my_tesla = Car("Tesla")
my_tesla.drive()
my_tesla.play_music("90.5 FM") 

my_yacht = Boat("Sunseeker")
my_yacht.sail()
my_yacht.play_music("Jazz Station") 