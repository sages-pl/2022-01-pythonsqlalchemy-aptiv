
result = 0

matrix = [[randint(0, 9) for y in ROWS]
          for x in COLS]

for row in matrix[6:-6]:
    result += sum(row[6:-6])
