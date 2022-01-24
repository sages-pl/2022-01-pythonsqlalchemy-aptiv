
s = pd.Series(
    data=np.random.randn(NUMBER),
    index=pd.date_range('2000-01-01', freq='D', periods=NUMBER))

result = s['2000-02-14':'2000-02']
