
class NegativeKelvinError(Exception):
    pass


def result(value):
    if value < 0:
        raise NegativeKelvinError
