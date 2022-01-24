

def clean(text: str) -> str:
    # Common format
    text = text.upper()

    # Remove unwanted whitespaces
    text = text.replace('\n', '')
    text = text.replace('\t', '')
    text = text.replace('     ', '')
    text = text.replace('    ', '')
    text = text.replace('   ', '')
    text = text.replace('  ', '')

    # Remove unwanted special characters
    text = text.replace('.', '')
    text = text.replace(',', '')
    text = text.replace('-', '')
    text = text.replace('|', '')

    # Remove unwanted text
    text = text.replace('ULICA', '')
    text = text.replace('UL', '')
    text = text.replace('TRZECIEGO', 'III')
    text = text.replace('3', 'III')

    # Formatting
    text = text.title()
    text = text.replace('Iii', 'III')
    text = text.replace('Ii', 'II')

    # Return
    return text.strip()



result = pd.Series(DATA).apply(clean)
