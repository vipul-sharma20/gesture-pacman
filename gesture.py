import cv2
import numpy as np

#img = cv2.imread('sample.jpg')
cap = cv2.VideoCapture(0)
PINK_MIN = np.array([120, 50, 50], np.uint8)
PINK_MAX = np.array([180, 180, 200], np.uint8)

while(cap.isOpened()):
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    img = cv2.GaussianBlur(img, (15, 15), 0)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #_, frame_threshed = cv2.threshold(grey, 127, 255,
    #                        cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    frame_threshed = cv2.inRange(hsv, PINK_MIN, PINK_MAX)

    contours,hierarchy = cv2.findContours(frame_threshed, 1, 2)
    max_area = 0
    if contours:
        for i in contours:
            area = cv2.contourArea(i)
            if area > max_area:
                max_area = area
                cnt = i

        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        centroid_x = (x + x+w)/2
        centroid_y = (y + y+h)/2

        cv2.line(img,(0,0),(1270,700),(255,0,0),5)
        cv2.line(img,(1270,0),(0,700),(255,0,0),5)
        #cv2.line(img,(0,20),(0,90),(255,0,0),5)
        cv2.imshow('Threshold', frame_threshed)
        cv2.imshow('blurred', img)


        #right move

    k = cv2.waitKey(10)
    if k == 27:
        break
