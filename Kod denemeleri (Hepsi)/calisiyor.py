from PIL import Image
import pytesseract
import cv2
import time


def show_webcam(mirror=True):
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        if mirror:
            img2 = cv2.copyMakeBorder(img, 100, 100, 100, 100, cv2.BORDER_REPLICATE)
        cv2.imshow('my webcam',img2)
        cv2.imwrite("Live_frame.jpg", img)
        # time.sleep(0.2)
        # ---->>>>< pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        img2 = Image.open("Live_frame.jpg")
        text = pytesseract.image_to_string(img, lang='tur')
        print(text)
        if cv2.waitKey(1) == 27:
            cv2.destroyAllWindows()
            break  # esc to quit


def main():
    show_webcam(mirror=True)


if __name__ == '__main__':
    main()

