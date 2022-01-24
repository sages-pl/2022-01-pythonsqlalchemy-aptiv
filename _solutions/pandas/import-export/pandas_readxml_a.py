
transform = XSLT(XML(TEMPLATE))
data = parse(StringIO(DATA))
html = str(transform(data))
dfs = pd.read_html(html)
result = dfs[0]
