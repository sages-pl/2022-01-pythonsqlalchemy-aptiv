
class Iris:
    def __init__(self, features, label):
        self.features = features
        self.label = label

    def __str__(self):
        total = sum(self.features)
        return f'{self.label} {total:.1f}'
