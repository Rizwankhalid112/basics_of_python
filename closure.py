def outer():
    message = "I am inner!"   
    def inner():
        print(message)         
    return inner

my_func = outer()
my_func()
print(my_func.__closure__)          