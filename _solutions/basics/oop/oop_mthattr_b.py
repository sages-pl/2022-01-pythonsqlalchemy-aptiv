
class Iris:
    def __init__(self, sepal_length, sepal_width,
                 petal_length, petal_width, species):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.species = species

    def get_numeric_values(self):
        return [x for x in vars(self).values() if type(x) is float]

    def total(self):
        return sum(self.get_numeric_values())

    def length(self):
        return len(self.get_numeric_values())

    def mean(self):
        return self.total() / self.length()

    def show(self):
        total = self.total()
        mean = self.mean()
        return f'{total=:.2f} {mean=:.2f} {self.species}'
