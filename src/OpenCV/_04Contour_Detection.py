import cv2, numpy


def main():
    image_dir = "/home/piyush/Pictures/OpenCV/contour/"
    image_name = "001"
    image_ext = ".jpg"
    image_path = f"{image_dir}{image_name}{image_ext}"

    # read rgb image
    # rgb_im = cv2.imread(image_path)

    ## OR

    webcam = cv2.VideoCapture(0)
    _, rgb_im = webcam.read()

    # convert to a graysclae image
    gray_im = cv2.cvtColor(rgb_im, cv2.COLOR_BGR2GRAY)

    # you can also directly read an image as grayscale
    # gray_im = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # use thresholding to convert it to a bniary image
    binary_im = cv2.adaptiveThreshold(
        gray_im, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 0)

    # retrive countours from the binary image
    contours, hierarchy = cv2.findContours(
        binary_im, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.RETR_TREE flag means the return object is tree of contours
    # outer contours are parents and inner ones are children represented as nodes
    # cv2.CHAIN_APPROX_SIMPLE is a method for finding contours

    # Drawing contours
    index = -1  # means draw all the contours
    # which indexth contour to draw out of all present in data structure returned by
    # findContours()

    thickness = 1  # thickness of contour line
    color = (255, 0, 255)  # magenta color for the contour line
    cont_im = numpy.copy(rgb_im)
    cv2.drawContours(cont_im, contours, index, color, thickness)

    # Show images
    cv2.imshow("Original image!", rgb_im)
    cv2.imshow("Gray Image!", gray_im)
    cv2.imshow("Binary Image!", binary_im)    
    cv2.imshow("Countours!", cont_im)
    cv2.waitKey(0)

    if "webcam" in locals():
        webcam.release()

if __name__ == "__main__":
    main()
