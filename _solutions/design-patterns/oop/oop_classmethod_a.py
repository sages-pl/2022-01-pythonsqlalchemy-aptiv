
class Timezone:
    when: datetime
    tzname: str

    def __init__(self, when):
        self.when = when

    @classmethod
    def convert(cls, dt: datetime):
        return cls(dt)


class CET(Timezone):
    tzname = 'Central European Time'


class CEST(Timezone):
    tzname = 'Central European Summer Time'
