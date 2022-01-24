
df = pd.read_csv(DATA, parse_dates=['datetime'])
df['year'] = df['datetime'].dt.year
df['month'] = df['datetime'].dt.month
calls = df[df['item'] == 'call']
result = calls.groupby(['year', 'month'])['duration'].sum()
