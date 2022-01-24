
class Distance:
    meters: int

    def __init__(self, meters):
        self.meters = meters

    def __format__(self, unit):
        result = self.meters
        if unit in ('cm', 'centimeter', 'centimeters'):
            result /= CENTIMETER
        elif unit in ('m', 'meter', 'meters'):
            result /= METER
        elif unit in ('km', 'kilometer', 'kilometers'):
            result /= KILOMETER
        return f'{result:.1f}'
