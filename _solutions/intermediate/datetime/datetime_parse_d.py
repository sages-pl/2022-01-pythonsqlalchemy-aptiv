
result = []

for line in DATA:
    try:
        dt = datetime.strptime(line, '%b %d, %Y %H:%M:%S')
    except ValueError:
        try:
            dt = datetime.strptime(line, '%B %d, %Y %H:%M')
        except ValueError:
            dt = datetime.strptime(line, '%B %d, %Y %H:%M:%S')
    result.append(dt)


# Alternative Solution
formats = [
    '%b %d, %Y %H:%M:%S',
    '%B %d, %Y %H:%M',
    '%B %d, %Y %H:%M:%S',
]

result = [datetime.strptime(line, fmt)
          for line, fmt in zip(DATA, formats)]


# Alternative Solution
result = []
formats = [
    '%b %d, %Y %H:%M:%S',
    '%B %d, %Y %H:%M',
    '%B %d, %Y %H:%M:%S',
]

for line, fmt in zip(DATA, formats):
    x = datetime.strptime(line, fmt)
    result.append(x)


# Alternative Solution
result = []
formats = [
    '%b %d, %Y %H:%M:%S',
    '%B %d, %Y %H:%M',
    '%B %d, %Y %H:%M:%S',
]

for line in DATA:
    for fmt in formats:
        try:
            x = datetime.strptime(line, fmt)
        except ValueError:
            pass
        else:
            result.append(x)
            break
    
