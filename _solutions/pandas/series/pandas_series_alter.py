
result = (
    pd.Series(DATA)
      .drop([2, 4, 6])
      .drop_duplicates()
      .reset_index(drop=True)
)


# ## Solution 1
# s = pd.Series(DATA)
# s.drop(2, inplace=True)
# s.drop(4, inplace=True)
# s.drop(6, inplace=True)
# s.drop_duplicates(inplace=True)
# s.reset_index(drop=True, inplace=True)
# result = s
#
# ## Solution 2
# s = pd.Series(DATA)
# s.drop([2, 4, 6], inplace=True)
# s.drop_duplicates(inplace=True)
# s.reset_index(drop=True, inplace=True)
#
#
# ## Solution 3
# s = pd.Series(DATA)
# s = s.drop([2, 4, 6])
# s = s.drop_duplicates()
# s = s.reset_index(drop=True)
#
# ## Solution 4
# s = pd.Series(DATA) \
#      .drop([2, 4, 6]) \
#      .drop_duplicates() \
#      .reset_index(drop=True)
