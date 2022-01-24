
result = (x for x in range(1, 34) if x % 3 == 0)
result = filter(odd, result)
result = map(cube, result)
result = list(result)
result = sum(result) / len(result)
