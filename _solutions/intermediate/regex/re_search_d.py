
hour = '([01][0-9]|2[0-3])'
minute = '[0-5][0-9]'
pattern = f'{hour}:{minute} UTC'
result = re.search(pattern, TEXT).group()

