class AddMixin:
    def add(self):
        result = self.a + self.b
        print(f"Addition of {self.a} and {self.b} is {result}")


class A():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def sub(self):
        resul=self.a-self.b
        print(f"Subtact is {resul}")
class SmartCalculator(A, AddMixin):
    pass

calc = SmartCalculator(10, 5)
calc.add() 
calc.sub()