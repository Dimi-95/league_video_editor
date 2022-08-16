import cv2 as cv



originalImage = cv.imread("samples/health_bar_in_bg_2.png")

width =  originalImage.shape[1]
height = originalImage.shape[0]


grayImage = cv.cvtColor(originalImage, cv.COLOR_BGR2GRAY)
focus_in_score = grayImage[0:25, int(width/2)+705:width-180]
resize = cv.resize(focus_in_score, (100,50))

(thresh, black_and_white_image) = cv.threshold(resize, 118, 255, cv.THRESH_BINARY )

cv.imshow("image", black_and_white_image)
cv.imwrite("samples/test_image.png", black_and_white_image)
cv.waitKey(0)


