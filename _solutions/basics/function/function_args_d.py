
def translate(text):
    return ''.join(PL.get(x, x) for x in text)
