
result = [iris(*features)
          for *features, label in DATA[1:]
          if (classname := label.capitalize())
          and (iris := globals()[classname])]


# Solution 2
result = []
for *features, label in DATA[1:]:
    if label == 'setosa':
        iris = Setosa(*features)
    elif label == 'virginica':
        iris = Virginica(*features)
    elif label == 'versicolor':
        iris = Versicolor(*features)
    result.append(iris)
