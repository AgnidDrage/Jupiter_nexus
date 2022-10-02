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

def processSingleChannel(path):
    imgOut = cv2.imread(path, cv2.IMREAD_COLOR)
    return imgOut

def changeContrast(img, alpha, beta):
    new_img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
    return new_img
    
def change_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.add(v,value)
    v[v > 255] = 255
    v[v < 0] = 0
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

def processMapImage(mapPath):
    image = cv2.imread(mapPath, flags=cv2.IMREAD_COLOR)
    #sharped image
    kernel = np.array([[0, -1, 0],
                    [-1, 5,-1],
                    [0, -1, 0]])

    image_sharp = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)

    hsv = cv2.cvtColor(image_sharp, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    lim = 255 - 20
    v[v > lim] = 255
    v[v <= lim] += 20
    image_bright = cv2.merge((h, s, v))

    # adjusting saturation
    h, s, v = image_bright[:,:,0], image_bright[:,:,1], image_bright[:,:,2]
    clahe = cv2.createCLAHE(clipLimit = 6, tileGridSize = (10,10))
    s = clahe.apply(s)
    hsv_img = np.dstack((h,s,v))

    #adjusting contrast
    h, s, v = hsv_img[:,:,0], hsv_img[:,:,1], hsv_img[:,:,2]
    clahe = cv2.createCLAHE(clipLimit = 7, tileGridSize = (10,10))
    v = clahe.apply(v)
    hsv_img2 = np.dstack((h,s,v))

    imgOut = cv2.cvtColor(hsv_img2, cv2.COLOR_HSV2RGB)

    return imgOut
