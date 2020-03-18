from PIL import ImageGrab
from PIL import Image
import numpy as np
import pytesseract
import argparse
import cv2
import os


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("output.avi", fourcc, 5.0, (1360, 768))

while(True):
        x = 760
        y = 968

        ox = 600
        oy = 600

        # screen capture
        img = ImageGrab.grab(bbox=(x, y, x + ox, y + oy))
        img_np = np.array(img)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        cv2.imshow("Screen", frame)
        out.write(frame)

        if cv2.waitKey(1) == 0:
                break

out.release()
cv2.destroyAllWindows()



