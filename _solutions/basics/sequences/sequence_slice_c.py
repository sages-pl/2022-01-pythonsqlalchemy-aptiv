
result = set()
result.update(a[::2])
result.update(b[::2])

# Alternative Solution
result = set()
result.update(a[::2], b[::2])
