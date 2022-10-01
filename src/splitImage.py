from heapq import merge
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./images/europa1/JNCE_2022272_45C00001_V01-raw.png', cv2.IMREAD_GRAYSCALE)

frames = [img[x:x+128,y:y+1648] for x in range(0,img.shape[0],128) for y in range(0,img.shape[1],1648)]

imagen2= np.zeros((26, 1648), np.uint8)

b = frames[0:len(frames):3]
g = frames[1:len(frames):3]
r = frames[2:len(frames):3]

b = [np.concatenate([i, imagen2], axis=0) for i in b]
g = [np.concatenate([i, imagen2], axis=0) for i in g]
r = [np.concatenate([i, imagen2], axis=0) for i in r]

b = np.concatenate(b, axis=0)
g = np.concatenate(g, axis=0)
r = np.concatenate(r, axis=0)

img = cv2.merge((r, g, b))

plt.imshow(img)
plt.show()