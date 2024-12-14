import cv2
import numpy as np

img = cv2.imread('eyes.jpg', cv2.IMREAD_COLOR)

if img is None:
    print("Error: Image not found.")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray_blurred = cv2.GaussianBlur(gray, (9, 9), 2)

detected_circles = cv2.HoughCircles(
    gray_blurred,
    cv2.HOUGH_GRADIENT, 1, 20, param1=50,
    param2=30, minRadius=1, maxRadius=40
)

if detected_circles is not None:
    detected_circles = np.uint16(np.around(detected_circles))

    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]

        cv2.circle(img, (a, b), r, (0, 255, 0), 2)

        cv2.circle(img, (a, b), 1, (0, 0, 255), 3)

    cv2.imshow("Detected Circles", img)
    cv2.waitKey(0)
else:
    print("No circles were detected.")

cv2.destroyAllWindows()