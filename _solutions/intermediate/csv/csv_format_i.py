
result = ''
keys = set()

for row in DATA:
    keys.update(row.keys())

header = sorted(keys)
result += ','.join(f'"{x}"' for x in header) + '\n'

for row in DATA:
    row = [row.get(x, '') for x in header]
    result += ','.join(f'"{x}"' for x in row) + '\n'
