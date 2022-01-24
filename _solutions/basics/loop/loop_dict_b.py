
header, *data = DATA
result = []

for row in data:
    pair = zip(header, row)
    result.append(dict(pair))
