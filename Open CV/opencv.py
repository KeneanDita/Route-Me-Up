import cv2 as cv
import os

img_path = os.path.join("assets", "1.jpg")
img = cv.imread(img_path)

if img is None:
    raise FileNotFoundError(f"Image not found at: {img_path}")

cv.imshow("Mustang", img)
cv.waitKey(0)
cv.destroyAllWindows()
