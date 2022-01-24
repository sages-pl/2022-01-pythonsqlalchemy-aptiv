
header, *data = DATA

data = []
for row in DATA:
    row = ','.join(str(x) for x in row)
    data.append(row + '\n')

with open(FILE, mode='w') as file:
    file.writelines(data)
