class A():
   def show(self):
    print("Hello From Class A")

class E():
   def show(self):
    print("Hello From Class E")

class B(A,E):
   def show(self):
    print("Hello From Class B")

class C(A,E):
   def show(self):
    print("Hello From Class C")

class D(C,B):
   def show(self):
    A.show(self)
    super(C,self).show()

obj=D()
print(D.__mro__)
obj.show()