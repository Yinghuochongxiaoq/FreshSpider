from PIL import Image, ImageFilter

# kitten = Image.open("python.jpg")
# blurryKitten = kitten.filter(ImageFilter.GaussianBlur)
# blurryKitten.save("kitten_blurred.png")
# blurryKitten.show()


image = Image.open("python.jpg")

# 对图片进行阈值过滤，然后保存
image = image.point(lambda x: 0 if x < 143 else 255)
image.save("python_point.png")
image.show()
