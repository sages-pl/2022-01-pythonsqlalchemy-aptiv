
header = pd.read_csv(DATA, nrows=0)
nrows, ncols, *class_labels = header.columns
label_encoder = dict(enumerate(class_labels))

result = (pd
    .read_csv(DATA, names=COLUMNS, skiprows=1, nrows=25)
    .replace(label_encoder)
)
