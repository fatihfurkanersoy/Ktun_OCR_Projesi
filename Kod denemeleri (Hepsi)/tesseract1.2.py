from PIL import Image
import pytesseract
import cv2
import time
import numpy as np

def show_webcam(mirror=True):
    cam = cv2.VideoCapture(1)
    while True:
        ret_val, img = cam.read()
        if mirror:
            img2 = cv2.copyMakeBorder(img, 100, 100, 100, 100, cv2.BORDER_REPLICATE)
        img3 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        img4 = cv2.threshold(img3, 250, 255, cv2.THRESH_TOZERO_INV)
        cv2.imshow("CAMERA", img4)
        kernel = np.ones((1, 1), np.uint8)
        img4 = cv2.dilate(img4, kernel, iterations=1)

        img4 = cv2.erode(img4, kernel, iterations=1)
        cv2.imwrite("Live_frame.jpg", img4)
        #time.sleep(0.2)
        pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        img5 = Image.open("Live_frame.jpg")
        text = pytesseract.image_to_string(img5, lang = 'tur')
        print(text)
        if cv2.waitKey(1) == 27:
            cv2.destroyAllWindows()
            break  # esc to quit


def main():
    show_webcam(mirror=True)

if __name__ == '__main__':
    main()


