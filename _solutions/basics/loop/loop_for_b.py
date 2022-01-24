
result = {}

for digit in DATA:
    if digit not in result:
        result[digit] = 1
    else:
        result[digit] += 1
