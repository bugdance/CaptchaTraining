import numpy as np
from PIL import Image
import io


def convert2gray(img):
    """
    图片转为黑白，3维转1维
    :param img: np
    :return:  灰度图的np
    """
    if len(img.shape) > 2:
        img = np.mean(img, -1)
    return img

def content2image(content):
    captcha_image = Image.open(io.BytesIO(content))
    # 转化为np数组
    image = np.array(captcha_image)
    image = convert2gray(image)
    image = image.flatten() / 255
    return image


def test(content):
    captcha_image = Image.open(io.BytesIO(content))

    return captcha_image

with open("test.jpg", "rb") as f:
    content = f.read()

image = test(content)
print(image)