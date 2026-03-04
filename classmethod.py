class Student:
    school_name="TUF"
    def __init__(self, name, age):
        self.name=name
        self.age=age
    
    def show(self):
        print(f"Studnet name is : {self.name}")
        print(f"Studnet age is : {self.age}")
    
    @classmethod
    def change_school_name(cls, name):
        cls.school_name=name

s1=Student("Rizwan",12)
s2=Student("Ali",10)

Student.change_school_name("Fast")
Student.show(s1)
print(Student.school_name)