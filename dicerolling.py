import random

def roll_dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    print(f'you rolled {dice1} and {dice2}')

while True:
    user_input = input("Do want want to roll(Yes/No): ")

    if user_input.upper() =='YES':
        roll_dice()
        user_input = input("Roll again? ")
        if user_input.upper() == "YES":
            roll_dice()
        else:
            quit()
    else:
        print('program ended')
        quit()