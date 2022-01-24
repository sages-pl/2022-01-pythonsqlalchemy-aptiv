
class Setosa(IrisInterface):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    species: str

    def __init__(self,
                 sepal_length: float,
                 sepal_width: float,
                 petal_length: float,
                 petal_width: float,
                 species: str) -> None:
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.species = species

    def _get_values(self):
        return [x for x in vars(self).values()
                  if isinstance(x, (float,int))]

    def mean(self) -> float:
        return self.sum() / self.len()

    def sum(self) -> float:
        return sum(self._get_values())

    def len(self) -> int:
        return len(self._get_values())
