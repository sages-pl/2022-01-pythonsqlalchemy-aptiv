
SELECT = {'setosa', 'versicolor'}


def sumif(features, label):
    if label in SELECT:
        return sum(features)
    else:
        return 0
