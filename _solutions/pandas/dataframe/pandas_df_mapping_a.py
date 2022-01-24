
df = pd.read_csv(DATA, parse_dates=['datetime'])
df['date'] = df['datetime'].dt.date
df['time'] = df['datetime'].dt.time
result = df


# ## Solution 2
# result = pd.read_csv(DATA, parse_dates=['datetime'])
# result['date'] = result['datetime'].map(lambda dt: dt.date())
# result['time'] = result['datetime'].map(lambda dt: dt.time())


# ## Solution 3
# result = pd.read_csv(DATA, parse_dates=['datetime'])
# result[['date', 'time']] = result['date'].map(str).str.split(expand=True)
