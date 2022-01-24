
with open(FILE, mode='w') as file:
    writer = csv.DictWriter(file, fieldnames=['firstname', 'lastname'],
                          delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL,
                          lineterminator='\n')

    writer.writeheader()
    writer.writerows(DATA)
