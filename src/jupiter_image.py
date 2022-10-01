import cv2
import matplotlib.pyplot as plt

image = cv2.imread("./images/JNCE_2022272_45C00001_V01-raw.png")

print(image)

plt.imshow(image)
plt.show()
