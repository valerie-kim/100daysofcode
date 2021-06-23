def add(*args): # arg is tuple
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(2,6,34,2,376,2,8,76,1,0))

def calculate(n, **kwargs): # kwargs is dict
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
    
calculate(2, add=3, multiply=5)