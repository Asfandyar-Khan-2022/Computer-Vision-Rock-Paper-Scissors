import time
import cv2
from keras.models import load_model
import numpy as np
from threading import Thread
import random 


model = load_model('keras_model.h5')                                                           # load in the pre-made data
cap = cv2.VideoCapture(0)                                     
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
stop_thread = False                                                                            # used to stop the thread once the winner or loser is decided


def get_computer_choice():                                                                     # select rock paper scissor randomly 
    return random.choice(['Rock', 'Paper', 'Sissors'])


def task1():                                                                                   # run the prediction model and make predictions 
    global prediction
    while True:                                                                                # run this until we are done with task 2
        ret, frame = cap.read()                                                                # capture camera footage
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)          # resize the captured footage
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1                           # Normalize the image, get better contrast
        data[0] = normalized_image
        prediction = model.predict(data, verbose = 0)                                          # make prediction
        cv2.imshow('frame', frame)                                                             # view everything displayed 

        if cv2.waitKey(1) & 0xFF == ord('q'):                                                  # press q to exit
            break
        elif stop_thread:                                                                      # when task 1 is done then it will be true
            break


def get_winner(computer_choice, user_choice):                                                  # return the results of the match 
    if computer_choice == 'Nothing':                                                           
        return 'You gotta show your hands'
    elif user_choice == 'Rock' and computer_choice == 'Paper':
        return 'You lost'
    elif user_choice == 'Paper' and computer_choice == 'Scissors':
        return 'You lost'
    elif user_choice == 'Scissors' and computer_choice == 'Rock':
        return 'You lost'
    elif user_choice == computer_choice:
        return 'it is a tie'
    else:
        return 'You win!'


computer_wins = 0
user_wins = 0
def task2():                                                                                   # check if the prediction matches the user input
    global stop_thread
    while computer_wins < 3 and user_wins < 3 :                                                # if either one wins three times, then end game and declare winner
        for i in range(3,0,-1):                                                                # countdown from 3 and delay for 3 seconds
            print(i)
            time.sleep(1)
        if prediction.argmax() == 0:                                                           # The most likely sign the user is making
            winner_count(get_winner(get_computer_choice(), 'Rock'))
        elif prediction.argmax() == 1:
            winner_count(get_winner(get_computer_choice(), 'Paper'))
        elif prediction.argmax() == 2:
            winner_count(get_winner(get_computer_choice(), 'Scissors'))
        elif prediction.argmax() == 3:
            winner_count(get_winner('Nothing', 'Nothing'))
    if computer_wins == 3:                                                                     # Check who won the game
        print ('The computer bested you!')
    else:
        print('You beat the robot. You win!')
    stop_thread = True


def winner_count(winner_loser_tie):                                                            # count the number of time either the computer or the user lost
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


t1 = Thread(target=task1)                                                                      # create thread and then start it
t1.start()
t2 = Thread(target=task2)
t2.start()
t1.join()                                                                                      # used to wait till the thread finishes before continuing 
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
