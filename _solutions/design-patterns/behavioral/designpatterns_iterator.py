
class Crew:
    def __init__(self):
        self.members = list()

    def __iadd__(self, other):
        self.members.append(other)
        return self

    def __iter__(self):
        self._current = 0
        return self

    def __next__(self):
        if self._current >= len(self.members):
            raise StopIteration
        result = self.members[self._current]
        self._current += 1
        return result
