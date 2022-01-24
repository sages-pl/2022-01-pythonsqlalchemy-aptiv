
class File:
    BUFFER_LIMIT: int = 100
    _content: list[str]
    filename: str

    def __init__(self, filename):
        self.filename = filename
        self._content = list()

    def __enter__(self):
        with open(self.filename, mode='w') as file:
            file.write('')
        return self

    def __exit__(self, *args):
        self._writefile()

    def _writefile(self):
        with open(self.filename, mode='a') as file:
            file.writelines(self._content)
            self._content = []

    def append(self, line):
        self._content.append(line + '\n')
        if getsizeof(self._content) > self.BUFFER_LIMIT:
            self._writefile()
