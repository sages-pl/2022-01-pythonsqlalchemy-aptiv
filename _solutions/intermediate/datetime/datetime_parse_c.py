
result = []

for line in DATA:
    try:
        dt = datetime.strptime(line, '%b %d, %Y %H:%M:%S')
    except ValueError:
        dt = datetime.strptime(line, '%B %d, %Y %H:%M')
    result.append(dt)
