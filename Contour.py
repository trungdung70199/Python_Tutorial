import cv2

image = cv2.imread('background.jfif')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawChessboardCorners(image, contours, -1, (0, 255, 0), 2)

cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
