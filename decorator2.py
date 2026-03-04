def timer(func):
    def wrapper(*args, **kwargs):  
        result = func(*args, **kwargs)
        return result
    return wrapper

@timer
def add(a, b):              
    print(a + b)

@timer
def full_name(first, last):  
    print(f"{first} {last}")

@timer
def student(name, age, city): 
    print(f"{name} {age} {city}")

@timer
def greet(name, greeting="Hello"):  
    print(f"{greeting} {name}")

add(2, 3)
full_name("Muhammad", "Rizwan")
student("Rizwan", 23, "TUF")
greet("Anas", greeting="Hi")