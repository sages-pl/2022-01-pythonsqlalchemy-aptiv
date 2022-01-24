
data = np.random.randint(10, 100, size=26)
alphabet = list(ASCII_LOWERCASE)
letter_position = median_low(alphabet)
position = alphabet.index(letter_position)

s = pd.Series(data, alphabet)
result = s[position-3:position+4]
