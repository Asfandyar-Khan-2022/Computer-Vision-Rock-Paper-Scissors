import time
import cv2
from keras.models import load_model
import numpy as np
from threading import Thread
import random 

cap = cv2.VideoCapture(0)  