
df = pd.read_csv(DATA)
class_labels = df.columns[2:]
label_encoder = dict(enumerate(class_labels))
df.columns = COLUMNS

df['Species'].replace(label_encoder, inplace=True)
df.loc[df['Petal length'] < 4.0, 'Petal length'] = np.nan
df = df.interpolate('linear')
df.dropna(inplace=True)
result = df.head(2)
