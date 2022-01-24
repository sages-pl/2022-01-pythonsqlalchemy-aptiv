
with open(FILE) as file:
    header = file.readline().strip().split(',')

    for line in file:
        *values, species = line.strip().split(',')
        values = tuple(float(x) for x in values)
        features.append(values)
        labels.append(species)
