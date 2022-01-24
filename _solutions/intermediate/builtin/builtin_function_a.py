
def average(args):
    if all(isinstance(x, float) for x in args):
        return sum(args) / len(args)


header, *data = DATA
result = {x:list() for x in header}

for row in data:
    for i, head in enumerate(header):
        result[head].append(row[i])

result = {key: average(value)
          for key, value in result.items()}
