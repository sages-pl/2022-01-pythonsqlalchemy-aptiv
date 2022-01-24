
values = []

for row in DATA[1:]:
    values.append(row[0])

result = sum(values) / len(values)
