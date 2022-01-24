
def isnumeric(*args, **kwargs):
    arguments = args + tuple(kwargs.values())

    if len(arguments) == 0:
        return False

    for arg in arguments:
        if type(arg) not in (float, int):
            return False

    return True
