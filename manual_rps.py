import random

def get_computer_choice():
    return random.choice(['Rock', 'Paper', 'Sissors'])

def get_user_choice():
    return str(input('Type either rock, paper or scissors: ')).lower().capitalize()

def get_winner(computer_choice, user_choice):
    while True:
        if user_choice == 'Rock' and computer_choice == 'Rock':
            return print('it is a tie!')
        elif user_choice == 'Rock' and computer_choice == 'Paper':
            return print('You lost')
        elif user_choice == 'Paper' and computer_choice == 'Scissors':
            return print('You lost')
        elif user_choice == 'Scissors' and computer_choice == 'Rock':
            return print ('You lost')
        else:
            return print('You win!')

def play():
    return get_winner(get_computer_choice(), get_user_choice())

play()