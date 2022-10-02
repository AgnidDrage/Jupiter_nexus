import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from astropy.visualization import make_lupton_rgb
from astropy.io import fits


def processImageByChannels(redPath, greenPath, bluePath):
    red = cv2.imread(redPath, cv2.IMREAD_GRAYSCALE)
    green = cv2.imread(greenPath, cv2.IMREAD_GRAYSCALE)
    blue = cv2.imread(bluePath, cv2.IMREAD_GRAYSCALE)

    red = np.around(red * 0.510).astype(np.uint8)
    green = np.around(green * 0.630).astype(np.uint8)
    blue = np.around(blue * 1).astype(np.uint8)

    return cv2.merge((red, green, blue))

def changeContrast(img, alpha, beta):
    new_img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
    return new_img

def increase_brightness(img, value):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img
    