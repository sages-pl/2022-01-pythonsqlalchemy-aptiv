
class Decoder(json.JSONDecoder):
    def __init__(self) -> None:
        super().__init__(object_hook=self.default)

    def default(self, data: dict) -> dict:
        for key, value in data.items():
            if key in ('destination_landing', 'launch_date'):
                data[key] = datetime.fromisoformat(value)
            elif key == 'born':
                data[key] = datetime.fromisoformat(value).date()
        return data


result = json.loads(DATA, cls=Decoder)
