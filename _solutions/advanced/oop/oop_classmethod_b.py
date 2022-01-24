
class CSVMixin:
    def to_csv(self) -> str:
        data = vars(self).values()
        return ','.join(data) + '\n'

    @classmethod
    def from_csv(cls, line: str):
        data = line.strip().split(',')
        return cls(*data)
