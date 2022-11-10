# Computer-Vision-Rock-Paper-Scissors

This project allows the user to show their hand to the camera and play rock, paper, scissors with the computer. The program has a preloaded model created using Teachable Machine. Which was provided with four labels. Rock, paper, scissor and nothing. With nothing being provided so that the model would not give false positives when the user was not proving a gesture. 

Once the game starts. The timer begins to countdown from 3. Giving the user a moment to provide their input. Once the input is registered by the model. The outcome of the match is saved. The final outcome is decided based on who was the first one to have three wins.

## Code breakdown

- First all the necessary libraries are imported, global variables declared and the keras model imported

- The first function selects a random value from a list

- The next task1 function is a thread used to perform multiple process at the same time. Purpose of using this techinque was so that the model can continuously work while delays were being used. 

- The task1 function also opens a window to show the user what the camera is seeing and makes a prediction using the model. Which is represented as a np.array. With the index correlating to the label. The function also works to normalise the image for processing

- Function get_winner finds if the user won the match or not. Returning a string value to represent loss or win. The function also return a string value in the event of a tie as well. Or if the user provided no input

- Function task2 checks what is the most likely gesture the user is aiming to make. It also checks to see if anyone has won the game. If they have then the global variable stop_thread is changed to reflect that. Which tells task1 to break and stop the game

- The final function counts how many times either the computer or the user lost. Counting up depending on the most appropriate action



<p align="center">
To play the game simply run camera_rps.py!
</p>