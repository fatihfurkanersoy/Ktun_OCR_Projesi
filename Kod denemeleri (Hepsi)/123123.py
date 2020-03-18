from PIL import Image
import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'
img = Image.open("1.png")
text = pytesseract.image_to_string(img)
print (text)