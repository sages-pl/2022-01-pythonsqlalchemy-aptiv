
def is_pesel_valid(pesel):
    if re.match(PATTERN, pesel):
        return True
    else:
        return False


def is_pesel_woman(pesel):
    if int(pesel[-2]) % 2 == 0:
        return True
    else:
        return False
