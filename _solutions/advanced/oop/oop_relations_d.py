
result = []
for astronaut in DATA:
    for i, mission in enumerate(astronaut.pop('missions'), start=1):
        for field,value in mission.items():
            column_name = f'mission{i}_{field}'
            astronaut[column_name] = value
    result.append(astronaut)
