
class Setosa(IrisAbstract):
    def __init__(self, sepal_length: float, sepal_width: float,
                 petal_length: float, petal_width: float) -> None:
        ...

    def mean(self) -> float:
        ...

    def sum(self) -> float:
        ...

    def len(self) -> int:
        ...
