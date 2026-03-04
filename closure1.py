def make_counter():
    count = 5

    def decrement():
        nonlocal count 
        count -= 1
        print(count)

    return decrement

obj1 = make_counter()
obj2 = make_counter()

obj1()
obj1()
obj1()

obj2()
obj2()

obj1()
obj1()
obj1()