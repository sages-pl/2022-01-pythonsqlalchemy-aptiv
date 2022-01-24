
class ValueRange:
    name: str
    min: float
    max: float
    value: float

    def __init__(self, name, min, max):
        self.name = name
        self.min = min
        self.max = max

    def __set__(self, parent, value):
        if value not in range(self.min, self.max):
            err = f'{self.name} is not between {self.min} and {self.max}'
            raise ValueError(err)
        self.value = value


class Astronaut:
    age = ValueRange('Age', min=28, max=42)
    height = ValueRange('Height', min=150, max=200)

    def __init__(self, name, age, height):
        self.name = name
        self.height = height
        self.age = age

    def __repr__(self):
        name = self.name
        age = self.age.value
        height = self.height.value
        return f'Astronaut({name=}, {age=}, {height=})'
