import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread("Test.png")

redImage = img
greenImage = img
blueImage = img

R = img[:, :, 0]
G = img[:, :, 1]
B = img[:, :, 2]

for i in range(3):
   	redImage[:, :, i] = R
   	greenImage[:, :, i] = G
   	blueImage[:, :, i] = B

print(blueImage)
mpimg.imsave('red5.png', img, cmap='Greys')

plt.show()