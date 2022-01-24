
header, *data = DATA
data = [dict(zip(header, row)) for row in data]

with open(FILE, mode='w') as file:
    json.dump(data, file)
