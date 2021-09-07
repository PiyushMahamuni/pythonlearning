#! /home/piyush/opencv_env/bin/python3

import cv2, numpy

def main():
    # download some tennis ball images to try this script and edit following fields
    # accordingly
    image_dir = "/home/piyush/Pictures/OpenCV/Tennis_Balls/"
    image_name = "002"
    image_ext = ".jpeg"
    image_path = f"{image_dir}{image_name}{image_ext}"
    image = cv2.imread(image_path)
    cv2.imshow(image_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Now converting the image into HSV format for color filtering
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imshow(image_name + " HSV", hsv_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # range of yellow in HSV format in OpenCV - 30 to 60 degrees
    yellow_lower = (30, 0, 0)
    # choose lower birghtness and saturation values for lower bound color
    yellow_upper = (60, 255, 255)
    # choose higher brightness and saturation values for upper bound color
    # Remember the HSV color space cone, you are setting up lower and upper bound planes
    # Hue values determine angles of bounding planes ( vertical ones)
    # value values determine height of bounding planes
    # saturation planes are curved surfaces(conical) of cone and saturation value determines
    # base radius of those curved surfaces
    # above bounds then cover all the possible range for yellow color i.e. all of the yellows

    # define a mask using the lower and upper bounds of the yellow colour
    mask = cv2.inRange(hsv_image, yellow_lower, yellow_upper)
    # the inRange performs thresholding and returns a grayscale image
    cv2.imshow("Masked", mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()