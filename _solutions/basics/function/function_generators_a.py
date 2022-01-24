
def odd(x):
    return x % 2


def cube(x):
    return x ** 3


# float: generator expr with numbers from 1 to 33 (inclusive) divisible by 3
#        filter out even numbers (leave even); cube result; calculate mean
result: float


numbers = (x for x in range(1, 34) if x % 3 == 0)
numbers = filter(odd, numbers)
numbers = map(cube, numbers)
numbers = list(numbers)
result = sum(numbers) / len(numbers)
