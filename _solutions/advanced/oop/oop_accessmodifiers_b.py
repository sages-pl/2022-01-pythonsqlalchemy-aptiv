
class Iris:
    def __init__(self, sepal_width: float, sepal_length: float,
                 petal_width: float, petal_length: float, species: str):
        self._sepal_width = sepal_width
        self._sepal_length = sepal_length
        self.__petal_width = petal_width
        self.__petal_length = petal_length
        self.species = species
