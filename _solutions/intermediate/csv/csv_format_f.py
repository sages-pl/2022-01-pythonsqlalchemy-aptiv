
result = []
header, *data = DATA.splitlines()
header = header.strip().split(',')

for line in data:
    line = line.strip().split(',')
    line = zip(header, line)
    result.append(dict(line))
