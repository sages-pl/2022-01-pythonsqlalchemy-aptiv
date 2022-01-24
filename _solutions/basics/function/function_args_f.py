
data = {str(k): v for k, v in DATA.items()}
data['-'] = 'minus'
data['.'] = 'and'


def pilot_say(number):
    return ' '.join(data[x] for x in str(number))
