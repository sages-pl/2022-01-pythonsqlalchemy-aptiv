
with open(FILE) as file:
    data = json.load(file)

result = [tuple(row.values()) for row in data]
