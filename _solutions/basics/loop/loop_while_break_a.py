
while True:
    guess = input('\nType number: ')

    if int(guess) > HIDDEN:
        print('Above')
    elif int(guess) < HIDDEN:
        print('Below')
    else:
        print('Exactly')
        break
