
result = []

for astronaut in DATA:
    for i, mission in enumerate(astronaut.pop('missions'), start=1):
        for field,value in mission.items():
            column_name = f'mission{i}_{field}'
            astronaut[column_name] = value
    result.append(astronaut)

fieldnames = set()
for row in result:
    fieldnames.update(row.keys())

with open(FILE, mode='w') as file:
    writer = csv.DictWriter(file, fieldnames=sorted(fieldnames), quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(result)
