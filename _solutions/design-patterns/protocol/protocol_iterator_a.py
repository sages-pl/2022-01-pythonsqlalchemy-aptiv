
@dataclass
class Astronaut:
    firstname: str
    lastname: str
    missions: tuple = ()

    def __iter__(self):
        self._iter_index = 0
        return self

    def __next__(self):
        if self._iter_index >= len(self.missions):
            raise StopIteration
        result = self.missions[self._iter_index]
        self._iter_index += 1
        return result
