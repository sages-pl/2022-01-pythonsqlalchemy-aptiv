
df = pd.read_csv(DATA, parse_dates=['datetime'], index_col=0)
df[['year', 'month']] = df['period'].str.split('-', expand=True)
df['month'] = df['month'].astype(int)
df['month'].replace(MONTHS, inplace=True)
result = df

# ## Solution 2
# result = pd.read_csv(DATA, parse_dates=['datetime'], index_col=0)
# result[['year', 'month']] = result['month'].str.split('-', expand=True)
# result['month'] = result['month_name'].astype(int).map(MONTHS)


# ## Solution 3
# result = pd.read_csv(DATA, parse_dates=['datetime'], index_col=0)
# result['year'] = result['period'].str[:4]
# result['month'] = result['period'].str[-2:]
# result['month'].astype(int).replace(MONTHS, inplace=True)
