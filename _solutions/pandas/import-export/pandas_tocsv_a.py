
result = pd.read_html(DATA, header=0)[0]
result = result.head(146).tail(11)
result['Event'].to_csv(FILE)
