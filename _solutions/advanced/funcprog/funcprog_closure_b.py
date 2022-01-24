
def check(func):
    def wrapper(*args, **kwargs):
        print('hello from wrapper')
    return wrapper


def hello():
    print('hello from function')


result = check(hello)
del check
result()
