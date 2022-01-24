
df = pd.read_csv(DATA, index_col=0)
df['Mission Date'] = df['Mission Date'] \
     .replace(MONTHS_PLEN, regex=True) \
     .apply(pd.to_datetime)

result = df
