
def typecheck(func):
    def validate(argname, argval):
        argtype = type(argval)
        expected = func.__annotations__[argname]
        if argtype is not expected:
            raise TypeError(f'"{argname}" is {argtype}, but {expected} was expected')

    def merge(*args, **kwargs):
        args = dict(zip(func.__annotations__.keys(), args))
        return kwargs | args          # Python 3.9
        # return {**args, **kwargs)}  # Python 3.7, 3.8

    def wrapper(*args, **kwargs):
        for argname, argval in merge(*args, **kwargs).items():
            validate(argname, argval)

        result = func(*args, **kwargs)
        validate('return', result)
        return result
    return wrapper
