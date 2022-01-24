
result = []

for line in DATA.splitlines():
    *values, species = line.strip().split(',')
    species = LABEL_ENCODER.get(species, species)
    row = values + [species]
    result.append(tuple(row))
