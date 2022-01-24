
class Mission:
    def __init__(self, year, name):
        self.year = year
        self.name = name

    def __eq__(self, other):
        return self.__class__ == other.__class__ \
           and self.year == other.year \
           and self.name == other.name
