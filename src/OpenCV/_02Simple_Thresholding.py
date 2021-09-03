#! /home/piyush/opencv_env/python3

import cv2
import numpy
import time

# CONSTANTS
FRAME_RATE = 30


def main():
    webcam = cv2.VideoCapture(0)
    frame_time = 1000 // FRAME_RATE

    thresh_val = 115

    while cv2.waitKey(frame_time) & 0XFF != ord('q'):
        _, image = webcam.read()
        # mirroring image
        image = image[:, -1::-1,]
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, thresh_image = cv2.threshold(
            image, thresh_val, 255, cv2.THRESH_BINARY)
        athresh_image = cv2.adaptiveThreshold(image,
                                              255,
                                              cv2.ADAPTIVE_THRESH_MEAN_C,
                                              cv2.THRESH_BINARY,
                                              thresh_val,
                                              5)

        cv2.imshow("Simple Thresholding", thresh_image)
        cv2.imshow("Adaptive Thresholding", athresh_image)

    webcam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
