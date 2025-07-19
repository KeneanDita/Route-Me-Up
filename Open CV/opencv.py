import cv2 as cv

img = cv.imread("Workfiles/1.jpg")
if img is None:
    raise FileNotFoundError("Image not found. Please check the file path.")

cv.imshow("Mustang", img)

cv.waitKey(0)
