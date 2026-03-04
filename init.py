class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age


class student(Person):
    def __init__(self,name,age):
        super().__init__(name,age)
        

    def show(self):
        print(f"Name is {self.name} and age is {self.age}")


p1 = student("Rizwan",20)
p1.show()


class Person1:
    def speak(self):
        print("Person is speaking")

class Student(Person1):
    def speak(self):  
        print("Student is speaking")

s1= Person1()
s1.speak()