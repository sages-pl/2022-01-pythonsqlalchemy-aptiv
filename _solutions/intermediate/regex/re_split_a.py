
pattern = r'</?p>'

for p in re.split(pattern, TEXT):
    if p.startswith('We choose to go to the moon'):
        result = p
