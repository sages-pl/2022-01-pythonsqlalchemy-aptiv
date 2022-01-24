
class Iris:
    features: list
    label: str

    def __init__(self, data):
        self.features = list(data[:-1])
        self.label = str(data[-1])

    def __repr__(self):
        features = self.features
        label = self.label
        return f'Iris({features=}, {label=})'
