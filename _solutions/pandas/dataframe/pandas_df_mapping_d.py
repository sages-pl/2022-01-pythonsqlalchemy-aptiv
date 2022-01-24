
LETTERS_PLEN.update({k.upper():v.upper()
                     for k,v in LETTERS_PLEN.items()})


def substitute(text):
    return ''.join(LETTERS_PLEN.get(x,x) for x in text)


df = pd.read_excel(io=DATA, sheet_name='Polish', header=1, index_col=0)
df = df.applymap(substitute)
df.columns = df.columns.map(substitute)
result = df
