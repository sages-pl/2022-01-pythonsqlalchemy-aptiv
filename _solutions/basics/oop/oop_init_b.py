
class Astronaut:
    def __init__(self, name, country, date):
        self.name = name
        self.country = country
        self.date = date


class SpaceAgency:
    def __init__(self, name, country, date):
        self.name = name
        self.country = country
        self.date = date


watney = Astronaut('Watney', 'USA', '1969-07-21')

nasa = SpaceAgency(name='NASA', country='USA', date='1958-07-29')
