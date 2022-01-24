
class Crew:
    def __init__(self, members=()):
        self.members = list(members)

    def __str__(self):
        return '\n'.join(str(x) for x in self.members)


class Astronaut:
    def __init__(self, name, experience=()):
        self.name = name
        self.experience = list(experience)

    def __str__(self):
        if not self.experience:
            return f'{self.name}'
        return f'{self.name} veteran of {self.experience}'

    def __repr__(self):
        return self.__str__()


class Mission:
    def __init__(self, year, name):
        self.year = year
        self.name = name

    def __repr__(self):
        return f'\n\t{self.year}: {self.name}'
