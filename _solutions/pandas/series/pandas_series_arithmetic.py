
s = pd.Series(
    data=np.random.randint(0, 9, size=5),
    index=list('abcde'))

s *= 10
s *= s

result = s
