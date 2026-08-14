import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# reading image
img = cv2.imread("cat.14.jpg") # Corrected filename from "ca1.14.jpg" to "cat.14.jpg"

# Check if the image was loaded successfully
if img is not None:
    cv2_imshow(img)

    # converting BGR image to HSV image
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2_imshow(hsv_img)

    # specifying range of blue color
    lower_blue = np.array([65, 0, 0])
    upper_blue = np.array([110, 255, 255])

    # creating mask for only blue color
    mask = cv2.inRange(hsv_img, lower_blue, upper_blue)
    cv2_imshow(mask)

    # returning result (mask) in blue color except the black one
    result = cv2.bitwise_and(img, img, mask = mask)
    cv2_imshow(result)
else:
    print("Error: 'cat.14.jpg' not found. Please ensure the image is available.")