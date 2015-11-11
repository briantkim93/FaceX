__author__ = 'Kim'

import cv2

from facex import *

def capture_image(show_image=True):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    if not ret:
        # show message box that something fatal occured, exit from this point
        pass

    if show_image:
        cv2.imshow("snapshot", frame)
        cv2.waitKey(0)

    cap.release()
    picname = util.get_random_name()

    picpath = "%s%s" % (util.temp_pic_dir, picname)
    cv2.imwrite(picpath, frame)

    return picpath