
result = [{'label': label, 'mean': mean(*features)}
          for *features, label in DATA[1:]]

# Alternative Solution
result = []
for *features, label in DATA[1:]:
    result.append({'label': label, 'mean': mean(*features)})

# Alternative Solution
result = [{'label': label,
           'mean': mean(*features)}
          for *features, label in DATA[1:]]

# Alternative Solution
result = [{'label': y, 'mean': mean(*X)}
          for *X,y in DATA[1:]]
