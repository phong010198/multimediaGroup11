import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread("Test.png")

def rgb_to_gray(image):
    grayImage = image
    R = image[:, :, 0]
    G = image[:, :, 1]
    B = image[:, :, 2]

    gray = R * 299/1000 + G * 587/1000 + B * 114/1000

    print(img)

    for i in range(3):
        grayImage[:,:,i] = gray

    return grayImage

grayImage = rgb_to_gray(img)

plt.imsave('Gray.png', grayImage)
plt.imshow(grayImage)
plt.show()