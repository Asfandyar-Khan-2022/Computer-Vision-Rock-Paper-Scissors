import time
import cv2
from keras.models import load_model
import numpy as np
from threading import Thread
import random 

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
def get_computer_choice():
    return random.choice(['Rock', 'Paper', 'Sissors'])

stop_thread = False

def task1():
    global prediction
    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data, verbose = 0)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        elif stop_thread:
            break

def get_winner(computer_choice, user_choice):
    if computer_choice == 'Nothing':
        return 'You gotta show your hands'
    elif user_choice == 'Rock' and computer_choice == 'Paper':
        return 'You lost'
    elif user_choice == 'Paper' and computer_choice == 'Scissors':
        return 'You lost'
    elif user_choice == 'Scissors' and computer_choice == 'Rock':
        return 'You lost'
    elif user_choice == computer_choice:
        return 'it is a tie!'
    else:
        return 'You win!'

computer_wins = 0
user_wins = 0
def task2():
    global stop_thread
    while computer_wins < 3 and user_wins < 3 :
        time.sleep(3)
        if prediction.argmax() == 0:
            winner_count(get_winner(get_computer_choice(), 'Rock'))
        elif prediction.argmax() == 1:
            winner_count(get_winner(get_computer_choice(), 'Paper'))
        elif prediction.argmax() == 2:
            winner_count(get_winner(get_computer_choice(), 'Scissors'))
        elif prediction.argmax() == 3:
            winner_count(get_winner('Nothing', 'Nothing'))
    if computer_wins == 3:
        print ('The computer bested you!')
    else:
        print('You beat the robot. You win!')
    stop_thread = True

def winner_count(winner_loser_tie):
    global computer_wins
    global user_wins
    if winner_loser_tie == 'You lost':
        print(winner_loser_tie)
        computer_wins += 1
    elif winner_loser_tie == 'You win!':
        print(winner_loser_tie)
        user_wins += 1
    else:
        print(winner_loser_tie)


        

t1 = Thread(target=task1)
t1.start()
t2 = Thread(target=task2)
t2.start()
t1.join()
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
