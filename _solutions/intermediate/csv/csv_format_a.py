
result = []

for line in DATA.splitlines():
    line = line.strip().split(',')
    result.append(tuple(line))
