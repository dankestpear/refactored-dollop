import random


def name_and_age():
    name = input('What is your name?')
    age = input('What is your age?')
    year100 = (2020-int(age)) + 100
    print('Hello, ' + name + ', you will turn 100 years old in the year ' + str(year100) + '.')
# name_and_age()


def odd_or_even():
    num_input = int(input('enter a number: '))
    if num_input % 2 != 0:
        print('odd')
    else:
        if num_input % 2 == 0:
            if num_input % 4 == 0:
                print('multiple of 4')
            else:
                print('even')
    num = int(input('enter a number'))
    check = int(input('enter another number'))
    if num % check == 0:
        print('the second number divides evenly into the first')
    else:
        print('the second number does not divide evenly into the first')
# odd_or_even()


def less_than_5(list_input):
    under_5 = []
    for i in list_input:
        if i < 5:
            under_5.append(i)
        else:
            pass
    print(under_5)
# less_than_5([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def divisor():
    num_input = int(input('enter a number: '))
    num_range = list(range(2, num_input))
    divisor_list = []
    for i in num_range:
        if num_input % i == 0:
            divisor_list.append(i)
        else:
            pass
    print(divisor_list)
# divisor()


def list_overlap():
    list1 = random.sample(range(0, 100), 20)
    list2 = random.sample(range(0, 100), 20)
    overlap = [i for i in list1 if i in list2]
    print(overlap)
# list_overlap()


def list_comprehension():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    b = [i for i in a if i % 2 == 0]
    print(b)
# list_comprehension()


def rock_paper_scissors():
    computer = ['rock', 'paper', 'scissors']
    while True:
        user_input = input('Choose rock, paper, or scissors, or quit to quit.')
        computer_choice = random.choice(computer)
        if user_input.lower() == 'quit':
            break
        elif user_input.lower() == 'rock':
            if computer_choice.lower() == 'rock':
                print('Tie!')
                continue
            elif computer_choice.lower() == 'paper':
                print('You lose!')
                continue
            elif computer_choice.lower() == 'scissors':
                print('You win!')
                continue
        elif user_input.lower() == 'paper':
            if computer_choice.lower() == 'rock':
                print('You win!')
                continue
            elif computer_choice.lower() == 'paper':
                print('Tie!')
                continue
            elif computer_choice.lower() == 'scissors':
                print('You lose!')
                continue
        elif user_input.lower() == 'scissors':
            if computer_choice.lower() == 'rock':
                print('You lose!')
                continue
            elif computer_choice.lower() == 'paper':
                print('You win!')
                continue
            elif computer_choice.lower() == 'scissors':
                print('Tie!')
                continue
        elif user_input.lower() == 'quit':
            break
        else:
            print('invalid input!')
            continue
    print('Thanks for playing!')
# rock_paper_scissors()


def guessing_game_one():
    guess = 0
    rand_int = random.randint(1, 10)
    num_guesses = 0
    while guess != rand_int:
        guess = input('Guess the number: ')
        if int(guess) < rand_int:
            print('Too low!')
            num_guesses += 1
            continue
        elif int(guess) > rand_int:
            print('Too high!')
            num_guesses += 1
            continue
        elif int(guess) == rand_int:
            num_guesses += 1
            print('You guessed it in', num_guesses, 'guesses!')
            play_again = input('Enter \'y\' to play again or \'q\' to quit.')
            if play_again.lower() == 'y':
                rand_int = random.randint(1, 10)
                num_guesses = 0
                guess = 0
                continue
            elif play_again.lower() == 'q':
                print('Thanks for playing!')
                break
# guessing_game_one()


def list_overlap_comprehensions():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = [i for i in set(a) if i in b]
    print(c)
# list_overlap_comprehensions()


def is_prime():
    num_input = int(input('Enter a number: '))
    prime_range = range(2, num_input)
    divisor_list = []
    for i in prime_range:
        if num_input % i == 0:
            divisor_list.append(i)
        else:
            pass
    if not divisor_list:
        print(num_input, 'is prime.')
    else:
        print(num_input, 'is not prime.')
# is_prime()


def Fibonacci():
    user_input = int(input('Enter how many Fibanocci numbers: '))
    fibonacci = [1, 1]
    i = len(fibonacci)
    if user_input == 1:
        print([1])
    elif user_input == 2:
        print(fibonacci)
    elif user_input > 2:
        fibonacci = [1, 1]
        while i < user_input:
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
            i = len(list(fibonacci))
        print(fibonacci)
# Fibonacci()


def list_maker():
    range1 = int(input('Enter the range: '))
    k1 = int(input('Enter the population: '))
    list1 = random.sample(range(0, range1), k1)
    return list1


def remove_duplicates():
    list1 = set(list_maker())
    print(list1)
# remove_duplicates()


def reverse_word_order(quote):
    quote = quote.split()
    print(' '.join(quote[::-1]))
# reverse_word_order("Ferb, I know what we're going to do today!")


def password_generator():
    while True:
        password = ''
        difficulty = input('Do you want a strong, medium, or weak password? Type \'quit\' to quit.')
        if difficulty.lower() == 'quit':
            print('Thank You!')
            break
        elif difficulty.lower() == 'strong' or 'medium' or 'weak':
            length = input('How long do you want the password to be?')
            word_list = """	
        way	
        year	
        work	
        government	
        day	
        man	men
        world	
        life	lives
        part	
        house	houses
        course	
        case	
        system	
        place	
        end	
        group	
        company	companies
        party	parties
        information	informations
        school	
        fact	
        money	moneys
        point	
        example	
        state	
        business	businesses
        night	
        area	areas
        water	
        thing	
        family	families
        head	
        hand	
        order	
        john	
        side	
        home	
        development	
        week	
        power	
        country""".split()
            character_list = r'`1234567890-=qwertyuiop[]\asdfghjkl;zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{' \
                             r'}|ASDFGHJKL:"ZXCVBNM<>? '
            num_list = '1234567890'
            if difficulty.lower() == 'strong':
                while len(password) < int(length):
                    password += random.choice(character_list)
            elif difficulty.lower() == 'medium':
                while True:
                    word_choice = random.choice(word_list)
                    if len(word_choice) > (int(length) - 2):
                        continue
                    else:
                        break
                password += word_choice
                while len(password) < int(length):
                    password += random.choice(character_list.lower())
            elif difficulty.lower() == 'weak':
                while True:
                    word_choice = random.choice(word_list)
                    if len(word_choice) > (int(length) - 2):
                        continue
                    else:
                        break
                password += word_choice
                while len(password) < int(length):
                    password += random.choice(num_list)
            print(''.join(password))
        else:
            print('invalid input')
            continue
# password_generator()










