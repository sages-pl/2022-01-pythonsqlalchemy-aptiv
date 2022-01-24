
class TypeCheck:
    def __init__(self, func) -> None:
        self._func = func

    def __call__(self, *args, **kwargs):
        self.check_arguments(*args, **kwargs)
        result = self._func(*args, **kwargs)
        self.check_result(result)
        return result

    def check_arguments(self, *args, **kwargs):
        arguments = kwargs | dict(zip(self._func.__annotations__.keys(), args))
        [self.validate(k, v) for k, v in arguments.items()]

    def check_result(self, result):
        self.validate('return', result)

    def validate(self, argname, argval) -> Exception | None:
        argtype = type(argval)
        expected = self._func.__annotations__[argname]
        if argtype is not expected:
            raise TypeError(f'"{argname}" is {argtype}, '
                            f'but {expected} was expected')
