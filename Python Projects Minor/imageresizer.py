import cv2
# opencv stands for open source computer vision library is a library used for computer vision and machine ler=arning tasks
# cv2 is the main module of opencv
img= cv2.imread("myimage.jpg")
# get original dimensions of image
print(f"original dimensions are: {img.shape}")
# resize the image
resized_img=cv2.resize(img,(2500,1500))
print(f"resized dimensions are: {resized_img.shape}")
cv2.imwrite("resized_image.jpg",resized_img)