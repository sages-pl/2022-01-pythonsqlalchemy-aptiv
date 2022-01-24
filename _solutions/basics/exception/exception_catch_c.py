
def result(degrees):
    try:
        degrees = int(degrees)
    except ValueError:
        raise TypeError('Invalid type, expected int or float')
    finally:
        print(degrees)
