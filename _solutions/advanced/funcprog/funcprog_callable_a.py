
def wrapper(*args, **kwargs):
    print('hello from wrapper')


def check(func):
    return wrapper
