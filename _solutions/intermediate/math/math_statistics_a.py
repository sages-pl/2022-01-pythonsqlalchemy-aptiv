
header, *data = DATA
sepal_length = [row[0] for row in data]
sepal_width = [row[1] for row in data]
petal_length = [row[2] for row in data]
petal_width = [row[3] for row in data]


def stats(values):
    return {
        'mean': mean(values),
        'stdev': stdev(values),
        'median': median(values),
        'variance': variance(values),
    }
