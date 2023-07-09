import random



while True:
    number = random.randint(1,5)


    user_number = int(input('Enter a number you have guessed (from 1 to 5): '))

    if user_number == number:
        print(number)
        print('correct guess')
        print(f'you guessed {user_number} and the number was {number}')



    else:
        print(number)
        print('Incorrect guess..')
        print(f'you guessed {user_number} and the number was {number}')
