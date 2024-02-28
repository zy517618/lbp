from skimage.feature import local_binary_pattern
#import skimage
import matplotlib.pyplot as plt
import cv2
import numpy as np
def test(list2):
    list2[1]=30
    return list2

def printIt(t):
    for i in range(len(t)):
        print (t[i])

if __name__=="__main__":
    radius = 3
    n_points = 8 * radius
    # 读文件
    image = cv2.imread('lena.jpg')
    #转换
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    lbp = local_binary_pattern(image, n_points, radius, method='ror')
    #plt.subplot(133)
    plt.imshow(lbp, cmap='gray')
    plt.show()