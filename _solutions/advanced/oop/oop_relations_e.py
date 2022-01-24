
result = []

for astronaut in DATA:
    astronaut.missions = [','.join(vars(x).values()) for x in astronaut.missions]
    astronaut.missions = ';'.join(astronaut.missions)
    result.append(vars(astronaut))
