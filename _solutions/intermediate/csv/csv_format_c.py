
result = []
header, *data = DATA.splitlines()
header = header.strip().split(',')
nrows, ncols, *class_labels = header
LABEL_ENCODER = dict(enumerate(class_labels))

for line in data:
    *values, species = line.strip().split(',')
    species = LABEL_ENCODER[int(species)]
    row = values + [species]
    result.append(tuple(row))
