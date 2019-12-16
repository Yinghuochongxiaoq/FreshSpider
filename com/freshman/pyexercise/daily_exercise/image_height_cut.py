# -*- coding:utf-8 -*-
""" 将一张图片填充为正方形后切为9张图 """
from PIL import Image


# 切图
def cut_image(image):
    width, height = image.size
    item_width = int(width)
    item_height = int(height / 19)
    box_list = []
    # (left,upper,right,lower)
    # 两重循环，生成*张图片基于原图的位置
    for i in range(0, 1):
        for j in range(0, 19):
            # print((i*item_width,j*item_width,(i+1)*item_width,(j+1)*item_width))
            box = (i * item_width, j * item_height, (i + 1) * item_width, (j + 1) * item_height)
            box_list.append(box)
    image_list = [image.crop(box) for box in box_list]
    return image_list


# 保存

def save_images(image_list):
    index = 1
    for image in image_list:
        image.save('2018-09-17_143849' + str(index) + '.png', 'PNG')
        index += 1


if __name__ == '__main__':
    file_path = "2018-09-17_143849.png"
    image = Image.open(file_path)
    image_list = cut_image(image)
    save_images(image_list)
