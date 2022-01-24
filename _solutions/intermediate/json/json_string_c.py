
header, *data = DATA
data = [dict(zip(header, row)) for row in data]

result = json.dumps(data)
