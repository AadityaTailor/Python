# from PIL import Image

# img=Image.open("a.jpg")
# transpose_img=img.transpose(Image.FLIP_LEFT_RIGHT)

# transpose_img.save("a1.jpg")
# print("done")

import cv2

img=cv2.imread("a.jpg")

clahe=cv2.createCLAHE()

gray_img=cv2.cvtColor(img.cv2.COLOR_BGR2GRAY)

enh_img=clahe.apply(gray_img)
cv2.imwrite("a2.jpg",enh_img)

print("Done")