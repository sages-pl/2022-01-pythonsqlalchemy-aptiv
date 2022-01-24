
def result(value):
    try:
        float(value)
    except ValueError:
        print('Invalid value')
