
result = ''
firstname, lastname = DATA[0].keys()
result += f'"{firstname}","{lastname}"\n'

for row in DATA:
    firstname, lastname = row.values()
    result += f'"{firstname}","{lastname}"\n'
