import random

def get_computer_choice():
    return random.choice(['Rock', 'Paper', 'Sissors'])
testing = 0
while 5 > testing:
    print(get_computer_choice())
    print(get_computer_choice())
    print(get_computer_choice())
    testing += 1

