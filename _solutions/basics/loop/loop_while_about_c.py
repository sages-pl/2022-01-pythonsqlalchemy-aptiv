
result = ''
i = 0

while i < len(DATA):
    letter = DATA[i]
    result += PL.get(letter, letter)
    i += 1
