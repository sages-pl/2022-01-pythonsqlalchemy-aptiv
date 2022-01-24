 1
for iris in json.loads(DATA):
    species = iris.pop('species')

    if species == 'setosa':
        cls = Setosa
    elif species == 'versicolor':
        cls = Versicolor
    elif species == 'virginica':
        cls = Virginica
    else:
        print('Not supported')

    result.append(cls(**iris))

# Solution 2
for row in json.loads(DATA):
    species = row.pop('species').capitalize()
    cls = globals()[species]
    iris = cls(**row)
    result.append(iris)

# Solution 3
result = [iris(**row)
          for row in json.loads(DATA)
          if (clsname := row.pop('species').capitalize())
          and (iris := globals()[clsname])]
