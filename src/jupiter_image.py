import cv2
import numpy as np
import matplotlib.pyplot as plt

blue = cv2.imread("./images/JNCE_2022272_45C00001_V01-blue.png", cv2.IMREAD_GRAYSCALE)
green = cv2.imread("./images/JNCE_2022272_45C00001_V01-green.png", cv2.IMREAD_GRAYSCALE)
red = cv2.imread("./images/JNCE_2022272_45C00001_V01-red.png", cv2.IMREAD_GRAYSCALE)

#print shapes
print("blue shape: ", blue.shape)
print("green shape: ", green.shape)
print("red shape: ", red.shape)

#merge 3 channels
img = cv2.merge((red, green, blue))
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#plot
plt.imshow(img)
plt.show()


