
class Encoder(json.JSONEncoder):
    def default(self, value: datetime) -> str:
        return value.isoformat()


result = json.dumps(DATA, cls=Encoder)
