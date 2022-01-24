
def celsius_to_kelvin(degrees):
    if type(degrees) in (int, float):
        return 273.15 + degrees

    if type(degrees) is tuple:
        return tuple(x + 273.15 for x in degrees)

    if type(degrees) is list:
        return list(x + 273.15 for x in degrees)

    if type(degrees) is set:
        return set(x + 273.15 for x in degrees)

    raise TypeError('Invalid argument')

## Solution 2
# if type(degrees) in (int, float):
#     return 273.15 + degrees
#
# if type(degrees) in (list, tuple, set):
#     cls = type(degrees)
#     return cls(x+273.15 for x in degrees)
#
# raise TypeError('Invalid argument')
