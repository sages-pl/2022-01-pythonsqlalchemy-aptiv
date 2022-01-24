
result = []

for astronaut in CREW:
    astronaut = vars(astronaut)
    missions = [','.join(str(x) for x in vars(mission).values())
                for mission in astronaut.pop('missions')]
    astronaut['missions'] = ';'.join(missions)
    result.append(astronaut)

# result = [astronaut | {'missions': ';'.join(values)}
#           for member in CREW
#           if (astronaut := vars(member))
#           and (values := [','.join(str(x) for x in vars(mission).values())
#                           for mission in astronaut.pop('missions')]) or True]


fieldnames = sorted(result[0].keys())

with open(FILE, mode='w') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(result)
