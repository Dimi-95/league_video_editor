from multiprocessing.connection import wait
from os import kill
import cv2 as cv
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

img = cv.imread("samples/test_image.png")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

width =  img.shape[1]
height = img.shape[0]

data = pytesseract.image_to_data(img)


for x,b in enumerate(data.splitlines()):
    if x != 0:
        b = b.split()
        if len(b) == 12:
            #value is a string
            value = b[11]
            print(b[11])
    
kills   = int(value[0])
deaths  = int(value[2])
assists = int(value[4])

print(f"kills: {kills + 1}, deaths: {deaths + 2}, assists: {assists + 3}")

cv.imshow("result", img)
cv.waitKey(0)