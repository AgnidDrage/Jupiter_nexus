import cv2
import numpy as np


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
    imgOut = cv2.cvtColor(imgOut, cv2.COLOR_BGR2RGB)
    return imgOut


def processMapImage(mapPath):
    image = cv2.imread(mapPath, flags=cv2.IMREAD_COLOR)
    # sharped image
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])

    image_sharp = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)

    hsv = cv2.cvtColor(image_sharp, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    lim = 255 - 20
    v[v > lim] = 255
    v[v <= lim] += 20
    image_bright = cv2.merge((h, s, v))

    # adjusting saturation
    h, s, v = image_bright[:, :, 0], image_bright[:,
                                                  :, 1], image_bright[:, :, 2]
    clahe = cv2.createCLAHE(clipLimit=6, tileGridSize=(10, 10))
    s = clahe.apply(s)
    hsv_img = np.dstack((h, s, v))

    # adjusting contrast
    h, s, v = hsv_img[:, :, 0], hsv_img[:, :, 1], hsv_img[:, :, 2]
    clahe = cv2.createCLAHE(clipLimit=7, tileGridSize=(10, 10))
    v = clahe.apply(v)
    hsv_img2 = np.dstack((h, s, v))

    imgOut = cv2.cvtColor(hsv_img2, cv2.COLOR_HSV2RGB)

    return imgOut


def processRawImage(rawPath):
    img = cv2.imread(rawPath, cv2.IMREAD_GRAYSCALE)
    frames = [img[x:x+128, y:y+1648]
              for x in range(0, img.shape[0], 128) for y in range(0, img.shape[1], 1648)]
    imagen2 = np.zeros((26, 1648), np.uint8)
    testFrame = np.zeros((128, 1648), np.uint8)
    testFrame2 = np.zeros(((128)*2, 1648), np.uint8)

    b = frames[0:len(frames):3]
    g = frames[1:len(frames):3]
    r = frames[2:len(frames):3]

    b = [np.concatenate([i, imagen2], axis=0) for i in b]
    g = [np.concatenate([i, imagen2], axis=0) for i in g]
    r = [np.concatenate([i, imagen2], axis=0) for i in r]
    b = np.concatenate(b, axis=0)
    g = np.concatenate(g, axis=0)
    r = np.concatenate(r, axis=0)

    g = np.concatenate([testFrame, g], axis=0)
    r = np.concatenate([testFrame2, r], axis=0)
    g = g[0:b.shape[0], 0:b.shape[1]]
    r = r[0:b.shape[0], 0:b.shape[1]]

    ImgOut = cv2.merge((b, g, r))

    return ImgOut


def changeContrast(img, alpha):
    if alpha >= 0:
        y = 0.0667*alpha + 1
    elif alpha < 0:
        y = 0.03333*alpha + 1
    new_img = cv2.convertScaleAbs(img, alpha=y, beta=1)
    return new_img


def change_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.add(v, value)
    v[v > 255] = 255
    v[v < 0] = 0
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img


def saturation(img, sat):
    # adjust the saturation of the input image
    y = 0.52*sat + 1
    h, s, v = img[:, :, 0], img[:, :, 1], img[:, :, 2]
    clahe = cv2.createCLAHE(clipLimit=y, tileGridSize=(10, 10))
    s = clahe.apply(s)
    hsv_img = np.dstack((h, s, v))
    return hsv_img
