
result = (x for x in range(1, 34) if x % 3 == 0)
result = filter(lambda x: x % 2, result)
result = map(lambda x: x ** 3, result)
result = list(result)
result = sum(result) / len(result)
