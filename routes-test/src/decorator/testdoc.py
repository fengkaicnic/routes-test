def decorator(fn):
    def wrapp(a, b):
        print ('input:', a, b)
        return fn(a, b)
    return wrapp

@decorator
def square_sum(a, b):
    return a**2 - b**2

@decorator
def square_diff(a):
    return a**2

print (square_sum(3, 4))
print (square_diff(2))