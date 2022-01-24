
result: list = []

for astronaut in json.loads(DATA):
    for i, address in enumerate(astronaut.pop('addresses'), start=1):
        for field,value in address.items():
            column_name = f'address{i}_{field}'
            astronaut[column_name] = value
    result.append(astronaut)
