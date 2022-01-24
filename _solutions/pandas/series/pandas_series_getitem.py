
s = pd.Series(
    data=np.random.randn(100),
    index=pd.date_range('2000-01-01', freq='D', periods=100))


result = {
    '2000-02-29': s['2000-02-29'],
    'first': s[0],
    'last': s[-1],
    'middle': s[s.size // 2],
}
