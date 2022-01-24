
class File:
    filename: str
    _content: list[str]

    def __init__(self, filename):
        self.filename = filename
        self._content = list()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        with open(self.filename, mode='w') as file:
            file.writelines(self._content)

    def append(self, line):
        self._content.append(line + '\n')
