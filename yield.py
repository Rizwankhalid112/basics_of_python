def square(self):
    for i in self:
        yield (i*i)

counter = square([1,2,3,4,5])
for kount in counter:
    print (kount)


nums=( i*i for i in range(6))
for num in nums:
    print(num)

def sub_gen():
    yield 1
    yield 2

def main_gen():
    yield from sub_gen()
    yield 3
for item in main_gen():
    print(item)
    
#gen = main_gen()
#print(next(gen))
#print(next(gen))
#print(next(gen))
