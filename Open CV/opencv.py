import cv2 as cv

img = cv.imread("Open CV/assets/1.jpg")

if img is None:
    raise FileNotFoundError(f"Image not found.")

cv.imshow("Mustang", img)
cv.waitKey(0)
cv.destroyAllWindows()
