
def result(age):
    try:
        age = float(age)
    except Exception:
        raise TypeError
    else:
        if age < ADULT:
            raise PermissionError
