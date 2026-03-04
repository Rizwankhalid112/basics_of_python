count = 3
def outer_func():
    count = 0
    
    def inner_func():
        global count
        count = 5
        print("Value of count is", count) 
        return count 

    inner_func() 
    return count

print(outer_func())
print(count)