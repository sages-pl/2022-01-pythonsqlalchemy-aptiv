
df = pd.read_csv(DATA)
df = df.sample(frac=1.0)
df.reset_index(drop=True, inplace=True)

result = df.tail(n=10)
