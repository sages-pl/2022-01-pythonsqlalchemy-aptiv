
def result(age):
    if type(age) not in (int, float):
        raise TypeError

    if age < 0:
        raise ValueError

    if age < ADULT:
        raise PermissionError
