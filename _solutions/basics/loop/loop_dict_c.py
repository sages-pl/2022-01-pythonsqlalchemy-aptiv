
features = []
labels = []
label_encoder = {}
lookup = {}
i = 0

for *X, y in DATA[1:]:
    if y not in lookup:
        label_encoder[i] = y
        lookup[y] = i
        i += 1
    labels.append(lookup[y])
    features.append(tuple(X))
