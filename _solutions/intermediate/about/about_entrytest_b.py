
result = []
header, *data = DATA

for row in data:
    paris = zip(header, row)
    result.append(dict(paris))
