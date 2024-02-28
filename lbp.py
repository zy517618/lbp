

from skimage.feature import local_binary_pattern
import skimage
import matplotlib.pyplot as plt
import cv2
import numpy as np
# settings for LBP
radius =10
n_points = 8 * radius

# 读取图像
image = cv2.imread('lena.jpg')

image1 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.subplot(131)
plt.imshow(image1)

# 转换为灰度图显示
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.subplot(132)
plt.imshow(image, cmap='gray')



lbp = local_binary_pattern(image, n_points, radius, method='ror')

plt.subplot(133)
plt.imshow(lbp, cmap='gray')
plt.show()
