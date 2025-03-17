import cv2
img=cv2.imread("img.jpg")
gry=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("bw.png",gry)