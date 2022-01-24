
class CSVMixin:
    def to_csv(self) -> str:
        return ','.join(vars(self).values()) + '\n'

    @classmethod
    def from_csv(cls, line: str):
        data = line.strip().split(',')
        return cls(*data)
