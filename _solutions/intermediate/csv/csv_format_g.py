
result = ''

for row in DATA:
    row = ','.join(row.values())
    result += str(row) + '\n'
