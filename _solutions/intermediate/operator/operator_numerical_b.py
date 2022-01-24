
@dataclass
class Astronaut:
    firstname: str
    lastname: str
    missions: list

    def __iadd__(self, other):
        self.missions.append(other)
        return self


@dataclass
class Mission:
    year: int
    name: str
