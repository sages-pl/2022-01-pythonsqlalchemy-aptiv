
a = TEXT.find(REMOVE)  # 10
b = a + len(REMOVE)  # 19
result = TEXT[:a] + TEXT[b:]
