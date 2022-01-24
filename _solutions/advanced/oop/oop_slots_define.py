
class Iris:
    __slots__ = ('sepal_length', 'sepal_width', 'petal_length',
                 'petal_width', 'species')

    def __init__(self, sepal_length, sepal_width,
                 petal_length, petal_width, species):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.species = species

    def __repr__(self):
        values = tuple(getattr(self, x) for x in self.__slots__)
        return f'Iris{values}'
