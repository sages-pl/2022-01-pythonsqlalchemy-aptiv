
for sentence in TEXT.split('.'):
    sentence = sentence.strip()
    words = sentence.split()
    letters = sentence.replace(',', '').replace(' ', '')
    characters = sentence.replace(',', '')
    comas = sentence.count(',')

    result['sentences'] += 1
    result['words'] += len(words)
    result['letters'] += len(letters)
    result['characters'] += len(characters)
    result['commas'] += comas

    for word in words:
        if word.endswith('ly'):
            result['adverbs'] += 1
