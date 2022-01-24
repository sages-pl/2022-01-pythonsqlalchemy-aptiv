
df = requests.get(DATA).json()
result = (pd.DataFrame(df['paths'])
            .transpose()
            .applymap(lambda x: x['summary'] if type(x) == dict else pd.NA))
