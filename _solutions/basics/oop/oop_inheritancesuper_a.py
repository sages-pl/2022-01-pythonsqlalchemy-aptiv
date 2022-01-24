
class Astronaut(Person):
    def __init__(self, name, mission):
        super().__init__(name)
        self.mission = mission

    def show(self):
        return f'{self.name}, {self.mission}'
