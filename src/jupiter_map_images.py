from colorsys import hsv_to_rgb
from tkinter import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance

# reading map image
image = cv2.imread(r"./images/europa1/JNCE_2022272_45C00001_V01-mapprojected.png", flags=cv2.IMREAD_COLOR)

# Resizing the image
scale_percent = 1
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dsize = (width, height)
cv2.resize(image, dsize)



#sharped image
kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
image_sharp = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)

#adjusting bright
def increase_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    print(hsv)
    h, s, v = cv2.split(hsv)
    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value
    final_hsv = cv2.merge((h, s, v))
    return final_hsv

image_bright = increase_brightness(image_sharp, value=20)

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

rgb = cv2.cvtColor(hsv_img2, cv2.COLOR_HSV2RGB)
plt.imshow(rgb)
plt.show()
