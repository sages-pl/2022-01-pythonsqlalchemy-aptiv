
class Mission:
    year: int
    name: str

    def __init__(self, year: int, name: str) -> None:
        self.year = year
        self.name = name

    def __eq__(self, other):
        return (self.year == other.year) \
           and (self.name == other.name)


class Astronaut:
    firstname: str
    lastname: str
    missions: list

    def __init__(self, firstname: str, lastname: str, missions: list) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.missions = missions


    def __contains__(self, flight):
        return flight in self.missions

