
data = []

for astronaut in DATA:
    astronaut = vars(astronaut)
    missions = [','.join(str(x) for x in vars(mission).values())
                for mission in astronaut.pop('missions')]
    astronaut['missions'] = ';'.join(missions)
    data.append(astronaut)

result = pd.DataFrame(data)
