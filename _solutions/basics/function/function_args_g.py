
def myrange(start, stop, step=1):
    current = start
    result = []

    while current < stop:
        result.append(current)
        current += step

    return result
