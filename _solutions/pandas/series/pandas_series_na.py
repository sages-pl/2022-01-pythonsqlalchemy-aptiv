
result = (
    pd.Series(DATA)
      .fillna(0, limit=1)
      .dropna()
      .reset_index(drop=True)
)


# Alternative Solution
# s = pd.Series(DATA)
# s = s.fillna(0, limit=1)
# s = s.dropna()
# s = s.reset_index(drop=True)

# Alternative Solution
# s = pd.Series(DATA)
# s.fillna(0, limit=1, inplace=True)
# s.dropna(inplace=True)
# s.reset_index(drop=True, inplace=True)
