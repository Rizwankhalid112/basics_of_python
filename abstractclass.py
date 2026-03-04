from abc import ABC, abstractmethod

class Device(ABC):
    def __init__(self, brand):
        self.brand = brand
        self._is_on = False

    def toggle_power(self):
        self._is_on = not self._is_on
        status = "ON" if self._is_on else "OFF"
        print(f"{self.brand} device is now {status}")

    @abstractmethod
    def operate(self):
        pass


class Laptop(Device):
    def operate(self):
        return f"{self.brand} Laptop is running code."

class Toaster(Device):
    def operate(self):
        return f"{self.brand} Toaster is browning bread."



my_laptop = Laptop("Apple")
my_laptop.toggle_power() 
print(my_laptop.operate()) 
my_toaster= Toaster("Haier")
print(my_toaster.operate())