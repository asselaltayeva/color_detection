import numpy as np
import cv2

def get_limits(color):

    c = np.uint8([[color]])  # BGR
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    hue = int(hsvC[0][0][0])

    lower_hue = max(hue - 10, 0)
    upper_hue = min(hue + 10, 179)

    lowerLimit = np.array([lower_hue, 100, 100], dtype=np.uint8)
    upperLimit = np.array([upper_hue, 255, 255], dtype=np.uint8)

    return lowerLimit, upperLimit
