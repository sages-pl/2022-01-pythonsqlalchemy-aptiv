
result = ''
data = [vars(x) for x in DATA]
header = data[0].keys()
result += ','.join(header) + '\n'

for row in data:
    row = map(str, row.values())
    result += ','.join(row) + '\n'
