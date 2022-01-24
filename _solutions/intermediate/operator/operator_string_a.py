
class Iris:
    features: list
    label: str

    def __init__(self, features, label):
        self.features = features
        self.label = label

    def __str__(self):
        label = self.label
        total = sum(self.features)
        return f'{label=}, {total=:.1f}'
