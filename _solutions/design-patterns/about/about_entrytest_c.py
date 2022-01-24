
result = set()

for *features, label in DATA[1:]:
    species = label.pop()

    if species.endswith(SUFFIXES):
        result.add(species)
