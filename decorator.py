import time 

def timer(func):
    def wrapper(*args, **kwargs):
        start=time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Total Time is : {end-start}")
    return wrapper

@timer
def add(a,b):
    result=a+b
    print(f"Add result is : {result}")
@timer
def multiply(a,b):
    result=a*b
    print(f"Multiply result is : {result}")

add(2,3)
multiply(2,3)