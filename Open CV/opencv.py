import cv2 as cv

img = cv.imread("Open CV/assets/1.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # convert to grayscale

if img is None:
    raise FileNotFoundError(f"Image not found.")
else:
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow("Gray Image", gray)
    cv.waitKey(0)
    cv.destroyAllWindows()

cv.imshow("Mustang", img)
cv.waitKey(0)
cv.destroyAllWindows()
