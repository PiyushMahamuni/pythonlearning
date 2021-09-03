#! /usr/bin/env python

import cv2
frame_rate = 30

def main():
    video_capture = cv2.VideoCapture(0)
    frame_time = 1000 // frame_rate
    # attach to the first video device connected to the computer
    while cv2.waitKey(frame_time) & 0XFF != ord('q'):
        ret, frame = video_capture.read()

        cv2.imshow("Image Feed", frame)
    
    video_capture.release()


if __name__ == "__main__":
    main()