import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./images/europa1/JNCE_2022272_45C00001_V01-raw.png')

frame = img[0:1648][0:128]

plt.imshow(frame)
plt.show()