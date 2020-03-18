import cv2
from PIL import Image
import pytesseract
import argparse
import os
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = Image.open("EkranAlıntısı.PNG", img)
text = pytesseract.image_to_string(img, lang='tur')
print(text)
cv2.imshow("ekranalintisi", EkranAlıntısı.PNG)