
def matches(opened_brackets, bracket):
    if not opened_brackets:
        return False

    opening_brackets = opened_brackets.pop()
    return PAIRS[opening_brackets] == bracket


def is_bracket_balanced(text):
    opened_brackets = []

    for character in text:
        if character in BRACKET_OPEN:
            opened_brackets.append(character)
        elif character in BRACKET_CLOSE:
            if not matches(opened_brackets, character):
                return False
    return not opened_brackets
