import cv2
import numpy as np

img = cv2.imread('sample.jpg')
cap = cv2.VideoCapture(0)
PINK_MIN = np.array([80, 0, 0], np.uint8)
PINK_MAX = np.array([170, 220, 220], np.uint8)

while(cap.isOpened()):
    ret, img = cap.read()
    #blurred = cv2.GaussianBlur(img, (35, 35), 0)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, frame_threshed = cv2.threshold(grey, 127, 255,
                            cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    #frame_threshed = cv2.inRange(hsv, PINK_MIN, PINK_MAX)

    cv2.imshow('Threshold', frame_threshed)
    #cv2.imshow('blurred', img)
    k = cv2.waitKey(10)
    if k == 27:
        break
