
data = []

for row in DATA:
    line = ','.join(row) + '\n'
    data.append(line)

with open(FILE, mode='wt') as file:
    file.writelines(data)
