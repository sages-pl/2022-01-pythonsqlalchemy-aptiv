
class Iris:
    def __init__(self, features, label):
        self.features = features
        self.label = label

    def sum(self):
        return sum(self.features)


for *features, label in DATA:
    iris = Iris(features, label)
    result[iris.label] = iris.sum()
