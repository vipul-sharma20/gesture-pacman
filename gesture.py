import cv2
import pyautogui
import numpy as np

cap = cv2.VideoCapture(0)
PINK_MIN = np.array([120, 50, 50], np.uint8)
PINK_MAX = np.array([180, 180, 200], np.uint8)
centroid_x = 0
centroid_y = 0
s = ''
move = ''

while(cap.isOpened()):

    ret, img = cap.read()
    img = cv2.flip(img, 1)

    #thresh = cv2.namedWindow('Threshold', cv2.WINDOW_NORMAL)
    orig = cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
    #img = cv2.GaussianBlur(img, (15, 15), 0)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    """
    Use this for thresholding using Otsu's Binarization method
    """
    #grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #_, frame_threshed = cv2.threshold(grey, 127, 255,
    #                        cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    frame_threshed = cv2.inRange(hsv, PINK_MIN, PINK_MAX)

    contours,hierarchy = cv2.findContours(frame_threshed, 1, 2)
    max_area = 0
    last_x = centroid_x
    last_y = centroid_y

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

        cv2.circle(img, (centroid_x, centroid_y), 2, (0,0,255), 2)
        cv2.line(img,(400,0),(400,700),(255,0,0),5)
        cv2.line(img,(900,0),(900,700),(255,0,0),5)
        cv2.line(img,(400,350),(900, 350),(255,0,0),5)

        #cv2.imshow('Threshold', frame_threshed)
        cv2.imshow('Original', img)


        """
        This method uses self defined quadrants. It finds the location of
        the centroid of bounding rectangle among the quadrants and simulates
        appropriate move.
        """
        # up-down move
        if centroid_x >= 400 and centroid_x <= 900:
            # up
            if centroid_y >= 0 and centroid_y <= 350:
                print 'up'
                pyautogui.press('up')
            # down
            if centroid_y >= 350 and centroid_y <=700:
                print 'down'
                pyautogui.press('down')

        # left-right move
        if centroid_y >= 0 and centroid_y <= 700:
            # left
            if centroid_x >= 0 and centroid_x <= 400:
                print 'left'
                pyautogui.press('left')
            # right
            if centroid_x >= 900:
                print 'right'
                pyautogui.press('right')


        """
        This method checks if there is a change in the coordinates of the
        centroid of bounding rectangle by some specific threshold in x or y
        axis and then simulates appropriate move.
        """

        ##right-left move
        #diff_x = centroid_x - last_x
        #if diff_x >= 30:
        #    print 'right'
        #    pyautogui.press('right')
        #    s = 'right'
        #elif diff_x <= -30:
        #    print 'left'
        #    pyautogui.press('left')
        #    s = 'left'

        ##up-down move
        #diff_y = centroid_y - last_y
        #if diff_y >= 30:
        #    print 'down'
        #    pyautogui.press('down')
        #    s = 'down'
        #elif diff_y <= -30:
        #    print 'up'
        #    pyautogui.press('up')
        #    s = 'up'
        #move = s

    k = cv2.waitKey(10)
    if k == 27:
        break
