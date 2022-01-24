
result = []

with open(FILE) as file:
    header = file.readline()
    reader = csv.DictReader(file,
                            fieldnames=FIELDNAMES,
                            delimiter=',',
                            quoting=csv.QUOTE_NONE)
    result = list(reader)
