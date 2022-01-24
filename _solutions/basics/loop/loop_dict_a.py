
result = {}

for lvl, titles in DATA.items():
    for title in titles:
        result[title] = str(lvl)
