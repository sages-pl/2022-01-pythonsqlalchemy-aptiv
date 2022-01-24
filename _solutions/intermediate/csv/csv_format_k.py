
result = ''
header = DATA[0].keys()
result += ','.join(header) + '\n'

for row in DATA:
    row = map(str, row.values())
    result += ','.join(row) + '\n'
