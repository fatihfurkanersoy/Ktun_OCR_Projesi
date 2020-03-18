import pytesseract
import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
# read the image using OpenCV
image = cv2.imread("a33.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gurultuazalt = cv2.bilateralFilter(gray, 9, 75, 75)
# cv2.namedWindow("Gürültü Temizleme islemi", cv2.WINDOW_NORMAL)
cv2.imshow("Gürültü Temizleme islemi", gurultuazalt)

histogram_e = cv2.equalizeHist(gurultuazalt)
# cv2.namedWindow("Histogram esitleme islemi", cv2.WINDOW_NORMAL)
cv2.imshow("Histogram esitleme islemi", histogram_e)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
morfolojikresim = cv2.morphologyEx(histogram_e, cv2.MORPH_OPEN, kernel, iterations=15)
# cv2.namedWindow("Morfolojik acilim", cv2.WINDOW_NORMAL)
cv2.imshow("Morfolojik acilim", morfolojikresim)

# Görüntü çıkarma (Morph görüntüsünü histogram eşitlenmiş görüntüsünden çıkarmak)
gcikarilmisresim = cv2.subtract(histogram_e, morfolojikresim)
# cv2.namedWindow("Goruntu cikarma", cv2.WINDOW_NORMAL)
cv2.imshow("Goruntu cikarma", gcikarilmisresim)

ret, goruntuesikle = cv2.threshold(gcikarilmisresim, 0, 255, cv2.THRESH_OTSU)
# cv2.namedWindow("Goruntu Esikleme", cv2.WINDOW_NORMAL)
cv2.imshow("Goruntu Esikleme", goruntuesikle)

canny_goruntu = cv2.Canny(goruntuesikle, 200, 250)
# cv2.namedWindow("Canny Edge", cv2.WINDOW_NORMAL)
cv2.imshow("Cbuuu ne laa", canny_goruntu)
canny_goruntu = cv2.convertScaleAbs(canny_goruntu)
cv2.imshow("Canny Edge", canny_goruntu)

# Kenarları güçlendirmek için genleşme
cekirdek = np.ones((3, 3), np.uint8)
# Genişletme için çekirdek oluşturma
gen_goruntu = cv2.dilate(canny_goruntu, cekirdek, iterations=1)
# cv2.namedWindow("Genisletme", cv2.WINDOW_NORMAL)
cv2.imshow("Genisletme", gen_goruntu)




pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# or you can use Pillow
# image = Image.open("test.png")
# get the string
string = pytesseract.image_to_string(image)
# print it
print(string)
# make a copy of this image to draw in
image_copy = image.copy()
# the target word to search for
target_word = ""
# get all data from the image
data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
# get the string
string = pytesseract.image_to_string(image)
# print it
print(string)
# get all occurences of the that word
word_occurences = [ i for i, word in enumerate(data["text"]) if word.lower() == target_word ]
for occ in word_occurences:
    # extract the width, height, top and left position for that detected word
    w = data["width"][occ]
    h = data["height"][occ]
    l = data["left"][occ]
    t = data["top"][occ]
    # define all the surrounding box points
    p1 = (l, t)
    p2 = (l + w, t)
    p3 = (l + w, t + h)
    p4 = (l, t + h)
    # draw the 4 lines (rectangular)
    image_copy = cv2.line(image_copy, p1, p2, color=(255, 0, 0), thickness=2)
    image_copy = cv2.line(image_copy, p2, p3, color=(255, 0, 0), thickness=2)
    image_copy = cv2.line(image_copy, p3, p4, color=(255, 0, 0), thickness=2)
    image_copy = cv2.line(image_copy, p4, p1, color=(255, 0, 0), thickness=2)
plt.imsave("all_dog_words.png", image_copy)
plt.imshow(image_copy)
plt.show()