
def clean(text):
    return (text

            # Convert to common format
            .upper()

            # Remove unwanted whitespaces
            .replace('\n', '')
            .replace('\t', '')
            .replace('     ', '')
            .replace('    ', '')
            .replace('   ', '')
            .replace('  ', '')

            # Remove unwanted special characters
            .replace('.', '')
            .replace(',', '')
            .replace('-', '')
            .replace('|', '')

            # Remove unwanted text
            .replace('ULICA', '')
            .replace('UL', '')
            .replace('TRZECIEGO', 'III')
            .replace('3', 'III')

            # Formatting
            .title()
            .replace('Iii', 'III')
            .replace('Ii', 'II')
            .strip())
