
df = pd.read_csv(DATA, delimiter=';')
df[['EV1', 'EV2', 'EV3']] = df['Participants'].str.split(', ', expand=True)
df['Duration'] = pd.to_timedelta(df['Duration'])

result = (pd.concat([
           df[['EV1', 'Duration']].rename(columns={'EV1': 'Astronaut'}),
           df[['EV2', 'Duration']].rename(columns={'EV2': 'Astronaut'}),
           df[['EV3', 'Duration']].rename(columns={'EV3': 'Astronaut'})
       ], axis='rows')
       .groupby('Astronaut')
       .sum()
       .sort_values('Duration', ascending=False))
