__author__ = 'Kim'

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

ret, frame = cap.read()
if ret:
    disp = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow("photo", frame)
    cv2.waitKey(0)

cap.release()
