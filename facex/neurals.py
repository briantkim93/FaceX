__author__ = 'Kim'

import cv2
import os
import numpy as np
from facex import *

cascade_path_face = "cascades/frontalFace10/haarcascade_frontalface_default.xml"
machine_neural = cv2.createLBPHFaceRecognizer()

neurals_trainmode = False

def get_faces(imgpath, min_neighbors=1):
    face_cascade = cv2.CascadeClassifier(cascade_path_face)
    img_pil = cv2.imread(imgpath)
    img = np.array(img_pil, 'uint8')
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    height, width = grayscale.shape[:2]

    faces = face_cascade.detectMultiScale(grayscale, 1.2, min_neighbors, cv2.cv.CV_HAAR_SCALE_IMAGE,
                                          (height / 8, width / 8))

    paths = []
    for (x, y, w, h) in faces:
        faceobj = img[y:y + h, x:x + w]
        basename = util.get_random_name()
        path = "%s%s" % (util.temp_pic_dir, basename,)
        cv2.imwrite(path, faceobj)
        paths.append(path)

    return paths


def neural_start():
    global machine_neural, neurals_trainmode

    if os.path.getsize(util.face_bin_arch) <= 1024:
        print "Train mode activated"
        neurals_trainmode = True
        return

    machine_neural.load(util.face_bin_arch)


def neural_update(img_paths, img_ids):
    global machine_neural, neurals_trainmode

    labels = np.array(img_ids)

    mats = []

    for path in img_paths:
        img_pil = cv2.imread(path, cv2.CV_LOAD_IMAGE_GRAYSCALE)
        img = np.array(img_pil, 'uint8')
        mats.append(img)

    if neurals_trainmode is True:
        machine_neural.train(mats, labels)
        machine_neural.save(util.face_bin_arch)
        neurals_trainmode = False
        return

    machine_neural.update(mats, labels)
    machine_neural.save(util.face_bin_arch)


def neural_getlabel(img_path):
    global machine_neural
    img = cv2.imread(img_path, cv2.CV_LOAD_IMAGE_GRAYSCALE)

    if neurals_trainmode is True:
        return -2

    return machine_neural.predict(img)

def neural_save():
    global machine_neural
    machine_neural.save(util.face_bin_arch)