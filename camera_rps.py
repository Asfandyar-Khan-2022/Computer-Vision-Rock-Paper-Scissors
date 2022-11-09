import time
import cv2
from keras.models import load_model
import numpy as np
from threading import Thread

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


def task1():
    global prediction
    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def task2():
    while True:
        time.sleep(5)
        if prediction.argmax() == 0:
            print ('Rock')
        elif prediction.argmax() == 1:
            print('Paper')
        elif prediction.argmax() == 2:
            print('Scissors')
        elif prediction.argmax() == 3:
            print('Nothing')
        

t1 = Thread(target=task1)
t1.start()
t2 = Thread(target=task2)
t2.start()
t1.join()
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
