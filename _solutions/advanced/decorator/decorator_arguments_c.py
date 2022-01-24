
def typecheck(check_return: bool = True):
    def decorator(func):
        def validate(argname, argval):
            argtype = type(argval)
            expected = func.__annotations__[argname]
            if argtype is not expected:
                raise TypeError(f'"{argname}" is {argtype}, '
                                f'but {expected} was expected')

        def wrapper(*args, **kwargs):
            arguments = kwargs | dict(zip(func.__annotations__.keys(), args))
            [validate(k, v) for k, v in arguments.items()]
            result = func(*args, **kwargs)
            if check_return:
                validate('return', result)
            return result

        return wrapper

    return decorator
