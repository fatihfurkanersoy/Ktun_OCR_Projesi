# USAGE
# python ocr.py --image images/example_01.png
# python ocr.py --image images/example_02.png  --preprocess blur
#PARAMETRE OLARAK Live_frame.png vermeyi unutma
# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os
import time


cam = cv2.VideoCapture(0)
while True:
    ret_val, img = cam.read()
    cv2.imshow('my webcam', img)
    cv2.imwrite("Live_frame.jpg", img)

    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
                    help="path to input image to be OCR'd")
    ap.add_argument("-p", "--preprocess", type=str, default="thresh",
                    help="type of preprocessing to be done")
    args = vars(ap.parse_args())

    # load the example image and convert it to grayscale
    image = cv2.imread(args["image"])
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Image", gray)
    gray = cv2.Canny(image, 100, 200)
    cv2.imshow("canny", gray)
    # check to see if we should apply thresholding to preprocess the
    # image
    if args["preprocess"] == "thresh":
        gray = cv2.threshold(gray, 0, 255,
                             cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    # make a check to see if median blurring should be done to remove
    # noise
    elif args["preprocess"] == "blur":
        gray = cv2.medianBlur(gray, 2)



    # write the grayscale image to disk as a temporary file so we can
    # apply OCR to it
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    # load the image as a PIL/Pillow image, apply OCR, and then delete
    # the temporary file
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    time.sleep(1)
    print(text)

    # show the output images
    # cv2.imshow("Image", image)
    cv2.imshow("Output", gray)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
