#coding=utf-8
"""
造物奇迹QQ2737499951
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image,ImageEnhance,ImageFilter


def showimg(img, isgray=False):
    plt.axis("off")
    if isgray == True:
        plt.imshow(img, cmap='gray')
    else:
        plt.imshow(img)
    plt.show()


img_name = 'test.jpg'
#去除干扰线
im = Image.open(img_name)
#图像二值化
im_gray = im.convert('L')
showimg(im_gray, True)
