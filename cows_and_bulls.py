def cows_and_bulls():
    print('cows = digit guessed correctly in the correct place\nbull = digit guessed correctly in the wrong place')
    user_input = ''
    running = True
    random_int = str(random.randint(1000, 10000))
    while running:
        print(random_int)
        cows = 0
        bulls = 0
        user_input = input('Guess the number: ')
        if not user_input.isdigit():
            print('invalid input')
            continue
        if len(user_input) != 4:
            print('invalid input', '\n')
            continue
        for i in range(0, 4):
            j = False
            if user_input[i] == random_int[i]:
                cows += 1
                j = True
            if not j and user_input[i] in random_int:
                bulls += 1
        print('COWS:', cows, '\n' + 'BULLS:', str(bulls) + "\n")
        if cows == 4:
            print('You got it! The number was ' + random_int + '.')
            while True:
                play_again = input('Enter \'y\' to play again or \'q\' to quit.')
                if play_again.lower() == 'q':
                    running = False
                    break
                elif play_again.lower() == 'y':
                    random_int = str(random.randint(1000, 10000))
                    break
                else:
                    print('invalid input')


cows_and_bulls()
