
class Iris:
    _sepal_length: float
    _sepal_width: float
    _petal_length: float
    _petal_width: float
    species: str

    def __init__(self, sepal_length, sepal_width, petal_length, petal_width, species):
        self._sepal_length = sepal_length
        self._sepal_width = sepal_width
        self._petal_length = petal_length
        self._petal_width = petal_width
        self.species = species
