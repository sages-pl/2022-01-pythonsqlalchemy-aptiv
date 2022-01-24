
class TypeCheck:
    def __init__(self, func) -> None:
        self._func = func

    def __call__(self, *args, **kwargs):
        self.check_arguments(*args, **kwargs)
        result = self._func(*args, **kwargs)
        self.check_result(result)
        return result

    def check_arguments(self, *args, **kwargs):
        for argname, argval in self.merge(*args, **kwargs).items():
            self.validate(argname, argval)

    def check_result(self, result):
        self.validate('return', result)

    def merge(self, *args, **kwargs):
        args = dict(zip(self._func.__annotations__.keys(), args))
        return kwargs | args          # Python 3.9
        # return {**args, **kwargs)}  # Python 3.7, 3.8

    def validate(self, argname, argval):
        argtype = type(argval)
        expected = self._func.__annotations__[argname]
        if argtype is not expected:
            raise TypeError(f'"{argname}" is {argtype}, but {expected} was expected')
