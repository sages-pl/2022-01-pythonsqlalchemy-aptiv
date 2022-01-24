
data = ','.join(str(x) for x in DATA) + '\n'

with open(FILE, mode='wt') as file:
    file.write(data)
