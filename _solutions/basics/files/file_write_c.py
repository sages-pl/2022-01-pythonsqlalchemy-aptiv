
data = '\n'.join(DATA) + '\n'

with open(FILE, mode='wt') as file:
    file.write(data)
