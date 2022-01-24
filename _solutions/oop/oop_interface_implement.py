
class Setosa(IrisInterface):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

    def __init__(self,
                 sepal_length: float,
                 sepal_width: float,
                 petal_length: float,
                 petal_width: float) -> None:
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width

    def mean(self) -> float:
        return self.sum() / self.len()

    def sum(self) -> float:
        return sum(self.__dict__.values())

    def len(self) -> int:
        return len(self.__dict__)
