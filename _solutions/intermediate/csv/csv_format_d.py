
result = []
header, *data = DATA.splitlines()
header = header.strip().split(',')
result.append(tuple(header))

for line in data:
    *values, species = line.strip().split(',')
    values = map(float, values)
    row = list(values) + [species]
    result.append(tuple(row))
