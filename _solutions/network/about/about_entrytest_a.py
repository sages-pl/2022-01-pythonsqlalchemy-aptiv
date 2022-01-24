
header, *data = DATA
result = []

for row in data:
    paris = zip(header, row)
    result.append(dict(paris))
