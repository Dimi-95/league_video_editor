from cgitb import reset
import cv2 as cv
import numpy as np

#Image one
img_1 = cv.imread("samples/test.png", cv.IMREAD_UNCHANGED)
width_1 = img_1.shape[0]
height_1 = img_1.shape[1]
crop_img_1 = img_1[0:25, int(height_1/2)+700:height_1-150]


# #Image two
# img_2 = cv.imread("samples/test_2.png")
# width_2 = img_2.shape[0]
# height_2 = img_2.shape[1]
# crop_img_2 = img_2[0:50, int(height_1/2)+500:height_1]

# cv.imshow("image_1", crop_img_1)
# cv.imshow("image_2", crop_img_2)

#Template
template = cv.imread("samples/numbers/0.png", cv.IMREAD_UNCHANGED)
#template = cv.resize(template, (25, 25))


#matching
result = cv.matchTemplate(template, crop_img_1, cv.TM_CCOEFF_NORMED )


#Detection Threshold
threshold = 0.23
locations = np.where(result >= threshold)

#Locating
location = list(zip(*locations[::-1]))

#Square
line_color = (0, 0, 255)
line_type = cv.LINE_4
template_w = template.shape[0]
template_h = template.shape[1]

#Creating the rectangle
rectangle = []
for loc in location:
    rect =  [int(loc[0]), int(loc[1]), template_w, template_h]
    rectangle.append(rect)
    rectangle.append(rect)


rectangle, weights = cv.groupRectangles(rectangle, 1, 0.5)
print("Number: ", rectangle)

for (x, y , w, h) in rectangle:
    top_left = (x, y)
    bottom_right =  (x + w, y + h)

    cv.rectangle(crop_img_1, top_left, bottom_right, line_color, line_type)

    center_x = x + int(w/2)
    center_y = y + int(h/2)


cv.imshow("Matches", crop_img_1)
cv.waitKey()